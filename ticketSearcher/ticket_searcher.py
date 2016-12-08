from data_parser import DataParser
from redis_client import RedisClient


class TicketSearcher:
    ALL_CITIES_KEY = 'all_czech_rep_cities'
    SEARCH_CONFIG_KEY = 'searchConfig'

    def __init__(self, search_restrictions):
        self.data_parser = DataParser()
        self.redis_client = RedisClient()
        self.search_restrictions = search_restrictions
        self.all_cities = self.redis_client.load_data(self.ALL_CITIES_KEY)

        if not self.all_cities:
            self.all_cities = self.data_parser.get_all_destination()

    def get_connections(self, source, destination, when):
        key = 'connections_{0}_{1}_{2}'.format(source, destination, when.strftime('%Y%m%d'))

        connections = self.redis_client.load_data(key)

        if not connections:
            connections = self.data_parser.get_connections(source, destination, when)
            self.redis_client.save_data(key, connections)

        connections = self.apply_search_config(connections)

        return connections

    def apply_search_config(self, search_result):
        if self.search_restrictions[self.SEARCH_CONFIG_KEY]:
            print(self.search_restrictions[self.SEARCH_CONFIG_KEY])

        return search_result

    def get_city_id(self, city_name):
        city_id = [city['id'] for city in self.all_cities if city['name'] == city_name]

        if not city_id:
            Exception('City ' + city_name + ' wasn\'t found in city dictionary')

        return city_id.pop(0)

    def get_city_name(self, city_id):
        city_name = [city['name'] for city in self.all_cities if city['id'] == city_id]

        if not city_name:
            raise Exception('City with ' + city_id + ' wasn\'t found in city dictionary')

        return city_name.pop(0)

    def get_best_connection(self, connections):
        result = {}
        filtered_connections = [connection for connection in connections if int(connection['free_spaces']) > 0]

        if filtered_connections:
            result = min(filtered_connections, key=lambda x: x['price'])
        return result

from data_parser import DataParser
from redis_client import RedisClient


class TicketSearcher:
    ALL_CITIES_KEY = "all_czech_rep_cities"

    def __init__(self):
        self.data_parser = DataParser()
        self.redis_client = RedisClient()

        self.all_cities = self.redis_client.load_data(self.ALL_CITIES_KEY)

        if not self.all_cities:
            self.all_cities = self.data_parser.get_all_destination()

    def get_connections(self, source, destination, when):
        key = 'connections_{0}_{1}_{2}'.format(source, destination, when.strftime('%Y%m%d'))

        connections = self.redis_client.load_data(key)

        if not connections:
            connections = self.data_parser.get_connections(source, destination, when)
            self.redis_client.save_data(key, connections)

        return connections

    def get_city_id(self, name):
        city_id = [city['id'] for city in self.all_cities if city['name'] == name]

        if not city_id:
            exit('City ' + name + ' wasn\'t found in city dictionary')

        return city_id.pop(0)

    def get_best_connection(self, connections):
        result = {}
        filtered_connections = [connection for connection in connections if int(connection['free_spaces']) > 0]

        if filtered_connections:
            result = min(filtered_connections, key=lambda x: x['price'])
        return result

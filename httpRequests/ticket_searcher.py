from data_parser import DataParser
from redis import StrictRedis
import json


class TicketSearcher:
    def __init__(self):
        self.data_parser = DataParser()
        self.all_cities = self.data_parser.get_all_destination()
        self.redis = StrictRedis(**{
            'host': '146.185.172.28',
            'password': 'razdvatrictyripet',
            'port': '6379'
        })

    def get_connections(self, source, destination, when):
        key = 'connections_{0}_{1}_{2}'.format(source, destination, when.strftime('%Y%m%d'))

        connections = self.redis.get(key)
        if not connections:
            connections = self.data_parser.get_connections(source, destination, when)
        else:
            connections = json.loads(connections.decode('utf-8'))

        self.redis.set(key, json.dumps(connections))
        self.redis.expire(key, 60 * 60)

        return connections

    def get_city_id(self, name):
        city_id = [city['id'] for city in self.all_cities if city['name'] == name]

        if not city_id:
            exit('City ' + name + ' wasn\'t found in city dictionary')

        return city_id.pop(0)

    def get_best_connection(self, connections):
        print(connections)
        return {}
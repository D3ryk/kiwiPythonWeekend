from redis import StrictRedis
import json


class RedisClient:
    def __init__(self):
        self.redis = StrictRedis(**{
            'host': '146.185.172.28',
            'password': 'razdvatrictyripet',
            'port': '6379'
        })

    def load_data(self, key):
        result = self.redis.get(key)

        if not result:
            result = {}
        else:
            result = self.json_deserialize(result)

        return result

    def save_data(self, key, value):
        return self.redis.set(
            key,
            self.json_serialize(value),
            60 * 60
        )

    def json_serialize(self, data):
        return json.dumps(data)

    def json_deserialize(self, data):
        return json.loads(data.decode('utf-8'))

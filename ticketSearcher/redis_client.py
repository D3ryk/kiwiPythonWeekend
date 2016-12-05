from redis import StrictRedis
import json


class RedisClient:
    REDIS_HOST = ''
    REDIS_PASSWD = ''
    REDIS_PORT = ''

    def __init__(self):
        self.redis = StrictRedis(**{
            'host': self.REDIS_HOST,
            'password': self.REDIS_PASSWD,
            'port': self.REDIS_PORT
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

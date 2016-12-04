from threading import Thread
from redis_client import RedisClient
import hashlib
import json
import os


class ConfigLoader(Thread):
    CONFIG_REDIS_KEY = 'honoluluConfigKey'
    CONFIG_NAME = 'config.json'
    CONFIG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config'))

    def __init__(self, config_file):
        super(ConfigLoader, self).__init__()
        self.redis_client = RedisClient()
        self.config = self.load_config_from_file(config_file)
        self.redis_client.save_data(self.CONFIG_REDIS_KEY, self.config)

    def run(self):
        while True:
            if self.is_config_file_changed():
                self.config = self.load_config()

    def load_config_from_file(self, file):
        with open(os.path.join(self.CONFIG_DIR, file)) as data_file:
            config = json.load(data_file)

        return config

    def load_config(self):
        config = self.redis_client.load_data(self.CONFIG_REDIS_KEY)

        if not config:
            config = self.load_config_from_file(self.CONFIG_NAME)
            self.redis_client.save_data(self.CONFIG_REDIS_KEY, config)

        return config

    def is_config_file_changed(self):
        new_config = self.load_config()
        old_config_md5 = hashlib.md5(self.redis_client.json_serialize(self.config).encode())
        new_config_md5 = hashlib.md5(self.redis_client.json_serialize(new_config).encode())

        if old_config_md5 != new_config_md5:
            return True

        return False

import logging
import os
from dotenv import load_dotenv
from app.models.singleton import SingletonMeta  # Adjust the import path as necessary

class Config(metaclass=SingletonMeta):
    _is_initialized = False

    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        # Prevent re-initialization
        if not Config._is_initialized:
            self.logger = logging.getLogger(__name__)
            self._location = self.get('LOCATION', 'default_location')
            self._device = self.get('DEVICE', 'default_device')
            self._mqtt_broker = self.get('MQTT_BROKER', 'localhost')
            self._mqtt_port = int(self.get('MQTT_PORT', 1883))
            self._mqtt_topic_temperature = f"iot/devices/{self._location}/{self._device}/temperature"
            self._mqtt_topic_humidity = f"iot/devices/{self._location}/{self._device}/humidity"
            self._mqtt_topic_status = f"iot/devices/{self._location}/{self._device}/status"
            self._mqtt_topic_commands = f"iot/devices/{self._location}/{self._device}/commands"
            Config._is_initialized = True

    @property
    def LOCATION(self):
        return self._location

    @property
    def DEVICE(self):
        return self._device

    @property
    def MQTT_BROKER(self):
        return self._mqtt_broker

    @property
    def MQTT_PORT(self):
        return self._mqtt_port

    @property
    def MQTT_TOPIC_TEMPERATURE(self):
        return self._mqtt_topic_temperature

    @property
    def MQTT_TOPIC_HUMIDITY(self):
        return self._mqtt_topic_humidity

    @property
    def MQTT_TOPIC_STATUS(self):
        return self._mqtt_topic_status

    @property
    def MQTT_TOPIC_COMMANDS(self):
        return self._mqtt_topic_commands

    @classmethod
    def initialize(cls):
        # Convenience method to explicitly initialize the Config
        # This method can be expanded to include more initialization parameters if needed
        cls()

    @staticmethod
    def get(key, default=None):
        return os.getenv(key, default)

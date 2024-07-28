import logging
import asyncio
import paho.mqtt.client as mqtt
from app.io.io_inventory import IOInventory
from app.helpers.temp_humidity_data_formatter import TempHumidityDataFormatter

class ThingsDataPublisher:
    def __init__(self, config):
        self.config = config
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_publish = self.on_publish
        self.logger = logging.getLogger(__name__)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.logger.info("Connected to MQTT Broker")
        else:
            self.logger.error(f"Failed to connect, return code {rc}")

    def on_disconnect(self, client, userdata, rc):
        self.logger.info("Disconnected from MQTT Broker")

    def on_publish(self, client, userdata, mid):
        self.logger.info(f"Message {mid} has been published")

    async def start(self):
        self.client.connect(self.config.MQTT_BROKER, self.config.MQTT_PORT, 60)
        self.client.loop_start()
        try:
            while True:
                self.publish_sensor_data()
                await asyncio.sleep(2)
        except asyncio.CancelledError:
            self.logger.info("Publisher stopped")
        finally:
            self.client.loop_stop()
            self.client.disconnect()

    def publish_sensor_data(self):
        temperature, humidity = IOInventory.read_dht11('dht11_sensor')
        status = "OK" if temperature is not None and humidity is not None else "DHT sensor not found, check wiring"
        
        message = TempHumidityDataFormatter.format_sensor_data(
            self.config.DEVICE,
            self.config.LOCATION,
            temperature,
            humidity,
            status
        )
        
        self.client.publish(self.config.MQTT_TOPIC_TEMPERATURE, message)
        self.logger.info(f"Published message: {message} to topic: {self.config.MQTT_TOPIC_TEMPERATURE}")

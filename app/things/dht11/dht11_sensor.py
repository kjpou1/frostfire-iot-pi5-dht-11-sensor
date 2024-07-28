import adafruit_dht
import logging

class DHT11Sensor:
    def __init__(self, pin):
        self.dht_sensor = adafruit_dht.DHT11(pin)
        self.logger = logging.getLogger(__name__)

    def read(self):
        """Reads temperature and humidity from the DHT-11 sensor."""
        try:
            temperature = self.dht_sensor.temperature
            humidity = self.dht_sensor.humidity
            if humidity is not None and temperature is not None:
                self.logger.info(f"Temperature: {temperature:.1f}C, Humidity: {humidity:.1f}%")
                return temperature, humidity
            else:
                self.logger.error("Failed to retrieve data from DHT-11 sensor")
                return None, None
        except RuntimeError as error:
            self.logger.error("RuntimeError: %s", error.args[0])
            return None, None

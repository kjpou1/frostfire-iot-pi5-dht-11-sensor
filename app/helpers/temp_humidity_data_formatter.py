from app.helpers.base_data_formatter import BaseDataFormatter

class TempHumidityDataFormatter(BaseDataFormatter):
    @staticmethod
    def format_sensor_data(device_id, location, temperature, humidity, status):
        data = {
            "temperature": temperature,
            "humidity": humidity
        }
        return BaseDataFormatter.format_data(device_id, location, data, status)

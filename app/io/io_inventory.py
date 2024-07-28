import logging
from app.models.singleton import SingletonMeta
from app.things.dht11.dht11_sensor import DHT11Sensor
import board

class IOInventory(metaclass=SingletonMeta):
    """
    IOInventory is a singleton class that manages I/O devices.
    It provides methods to add devices, retrieve them, and control their states.
    """
    _is_initialized = False
    _devices = {}

    def __init__(self):
        """
        Initializes the IOInventory and logs device info.
        This is called only once due to the singleton pattern.
        """
        if not IOInventory._is_initialized:
            self.logger = logging.getLogger(__name__)
            self.logger.info(f"Initializing IO Inventory")
            IOInventory._is_initialized = True

    @classmethod
    def initialize(cls):
        """
        Convenience method to explicitly initialize the IOInventory.
        This can be expanded to include more initialization parameters if needed.
        """
        cls()

    @classmethod
    def add_device(cls, name, device):
        """
        Adds a device to the inventory.
        
        :param name: The name of the device.
        :param device: The device instance to add.
        """
        cls._devices[name] = device

    @classmethod
    def get_device(cls, name):
        """
        Retrieves a device from the inventory by name.
        
        :param name: The name of the device to retrieve.
        :return: The device instance, or None if not found.
        """
        return cls._devices.get(name)

    @classmethod
    def read_dht11(cls, name):
        """
        Reads the DHT-11 sensor data.
        
        :param name: The name of the DHT-11 sensor device.
        :return: Tuple containing temperature and humidity, or (None, None) if an error occurs.
        """
        device = cls.get_device(name)
        if device:
            return device.read()
        else:
            cls._log_device_not_found(name)
            return None, None

    @classmethod
    def _log_device_not_found(cls, name):
        """
        Logs an error if a device is not found in the inventory.
        
        :param name: The name of the device not found.
        """
        logger = logging.getLogger(__name__)
        logger.error(f"Device '{name}' not found in inventory")

# Initialize the IOInventory and add the DHT11 device
IOInventory.initialize()
IOInventory.add_device('dht11_sensor', DHT11Sensor(board.D4))

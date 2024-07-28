import paho.mqtt.client as mqtt
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# MQTT settings (should match the publisher settings)
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC_TEMPERATURE = 'iot/devices/study/temp_humidity_sensor/temperature'
MQTT_TOPIC_HUMIDITY = 'iot/devices/study/temp_humidity_sensor/humidity'
MQTT_TOPIC_STATUS = 'iot/devices/study/temp_humidity_sensor/status'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info("Connected to MQTT Broker")
        # Subscribe to the topics
        client.subscribe(MQTT_TOPIC_TEMPERATURE)
        client.subscribe(MQTT_TOPIC_HUMIDITY)
        client.subscribe(MQTT_TOPIC_STATUS)
    else:
        logger.error(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    logger.info(f"Received message from topic {msg.topic}: {msg.payload.decode()}")

def on_disconnect(client, userdata, rc):
    logger.info("Disconnected from MQTT Broker")

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()

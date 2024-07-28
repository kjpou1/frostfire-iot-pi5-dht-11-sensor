# Frostfire IoT Pi5 DHT-11 Sensor

This project is a Python-based IoT application for reading temperature and humidity data from a DHT-11 sensor connected to a Raspberry Pi 5 and publishing the data using MQTT. It integrates with an IoT Hub for centralized data collection and management.

For centralized data collection and management, refer to the [FrostFire IoT Hub Project](https://github.com/kjpou1/frostfire-iot-hub.git).

## Table of Contents

- [Frostfire IoT Pi5 DHT-11 Sensor](#frostfire-iot-pi5-dht-11-sensor)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Command Line Arguments](#command-line-arguments)
    - [Examples](#examples)
  - [Configuration](#configuration)
  - [Published Data](#published-data)
    - [Data Format](#data-format)
    - [Example JSON](#example-json)
  - [Shell Script](#shell-script)
    - [Shell Script Examples](#shell-script-examples)
    - [Running the Shell Script](#running-the-shell-script)
  - [Docker Setup](#docker-setup)
    - [Docker Installation](#docker-installation)
    - [Docker Compose](#docker-compose)
  - [License](#license)
  - [References](#references)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/kjpou1/frostfire-iot-pi5-dht-11-sensor.git
    cd frostfire-iot-pi5-dht-11-sensor
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment file**

    Copy or rename the `example_env` file to `.env` before running

    ```bash
    cp example_env .env
    ```

## Usage

To run the IoT application, use the provided `run.py` script with appropriate command-line arguments.

### Command Line Arguments

Currently, there are no specific command-line arguments defined for this project. Ensure the `.env` file is configured correctly.

### Examples

To run the publisher:

```bash
python run.py
```

To run the subscriber:

```bash
python tests/subscriber.py
```

## Configuration

The configuration settings are managed through environment variables and can be set in a `.env` file in the root directory of the project. 
Example `.env` file:

``` 
LOCATION=study
DEVICE=temp_humidity_sensor
MQTT_BROKER=localhost
MQTT_PORT=1883
```

> [!NOTE]
> An `example_env` file is provided to get started.  Copy the file to `.env` before running:

## Published Data

### Data Format

The data published by the IoT application is in JSON format and includes the following fields:

- **device_id**: A unique identifier for the device.
- **location**: The location where the device is installed.
- **data**: An object containing the sensor data, including:
  - **temperature**: The temperature reading from the sensor (in Celsius).
  - **humidity**: The humidity reading from the sensor (in percentage).
  - **timestamp**: The timestamp of when the data was recorded (in ISO 8601 format).
  - **status**: The status of the sensor (e.g., "OK", "DHT sensor not found, check wiring").

### Example JSON

Here is an example of the JSON data published by the IoT application:

```json
{
  "device_id": "temp_humidity_sensor",
  "location": "study",
  "data": {
    "temperature": 22.5,
    "humidity": 45.0,
    "timestamp": "2024-07-28T06:20:30Z",
    "status": "OK"
  }
}
```

## Shell Script

A shell script `run.sh` is provided to automate the execution of the script.

### Shell Script Examples

Example `run.sh`

```bash
#!/bin/bash
source ./.venv/bin/activate
python ./run.py
deactivate
```

### Running the Shell Script

To run the script:

```bash
./run.sh
```

## Docker Setup

### Docker Installation

To build and run the application using Docker, you need to have Docker and Docker Compose installed on your machine.

1. **Install Docker:**
   Follow the instructions on the [Docker website](https://docs.docker.com/get-docker/) to install Docker.

2. **Install Docker Compose:**
   Follow the instructions on the [Docker Compose website](https://docs.docker.com/compose/install/) to install Docker Compose.

### Docker Compose

1. **Build and run the application:**

    ```bash
    DOCKERFILE=Dockerfile docker-compose up --build  # For general use
    DOCKERFILE=Dockerfile.pi docker-compose up --build  # For Raspberry Pi
    ```

2. **Stop the application:**

    ```bash
    docker-compose down
    ```

3. **Review and update the `.dockerignore` file**

    Ensure the `.dockerignore` file in the root directory of the project includes necessary patterns to exclude unnecessary files and directories. Below is an example of what it might include:


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## References

For centralized data collection and management, refer to the [IoT Hub Project](https://github.com/kjpou1/frostfire-iot-hub.git).

This project integrates with the IoT Hub to send sensor data for centralized processing and analysis.

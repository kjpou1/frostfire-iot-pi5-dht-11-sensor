# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    libgpiod2 \
    python3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove build-essential libssl-dev libffi-dev python3-dev

# Make port 1883 available to the world outside this container
EXPOSE 1883

# Define environment variable
ENV MQTT_BROKER=localhost
ENV MQTT_PORT=1883
ENV LOCATION=study
ENV DEVICE=temp_humidity_sensor

# Run run.py when the container launches
CMD ["python", "run.py"]

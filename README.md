# Data Pipeline Messenger

This Python project provides an easy-to-use framework for sending data to multiple services like Kafka, RabbitMQ, and REST APIs. The code is designed to be extensible, allowing you to integrate with other messaging services like AWS SQS, Google Pub/Sub, and MQTT.

## Features

- **Kafka Integration**: Send JSON/dict data to Kafka topics.
- **RabbitMQ Integration**: Publish messages to RabbitMQ queues.
- **REST API Integration**: Post data to REST APIs.
- Extensible architecture to integrate with other messaging services.
  
## Installation

First, clone the repository:

```bash
git clone https://github.com/Kaiser-14/data-pipeline-messenger
cd data-pipeline-messenger
```


## Requirements

### Required Libraries

- `kafka-python`
- `pika`
- `requests`

You can install these dependencies manually using pip:

```bash
pip install kafka-python pika requests
```

Or

```bash
pip install -r requirements.txt
```

## Configuration

Each service requires specific configurations:

- Kafka: `bootstrap_servers` (list), `topic` (string)
- RabbitMQ: `host` (string), `queue` (string)
- REST API: `url` (string)

## Usage

### Example: Sending Data to Kafka

```python
from data_pipeline import send_data

data = {"key": "value"}

kafka_config = {
    "bootstrap_servers": ["localhost:9092"],
    "topic": "test_topic"
}

send_data("kafka", kafka_config, data)
```

### Example: Sending Data to RabbitMQ

```python
from data_pipeline import send_data

data = {"key": "value"}

rabbitmq_config = {
    "host": "localhost",
    "queue": "test_queue"
}

send_data("rabbitmq", rabbitmq_config, data)
```

### Example: Sending Data to a REST API

```python
from data_pipeline import send_data

data = {"key": "value"}

restapi_config = {
    "url": "http://localhost:5000/api/data"
}

send_data("restapi", restapi_config, data)
```
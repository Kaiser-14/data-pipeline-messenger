import json
import requests
from kafka import KafkaProducer
import pika


# Function to send data to Kafka
def send_to_kafka(bootstrap_servers, topic, data):
	producer = KafkaProducer(
		bootstrap_servers=bootstrap_servers,
		value_serializer=lambda v: json.dumps(v).encode('utf-8')
	)
	future = producer.send(topic, data)
	result = future.get(timeout=10)
	producer.close()
	print(f"Data sent to Kafka topic {topic}: {result}")


# Function to send data to RabbitMQ
def send_to_rabbitmq(host, queue, data):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
	channel = connection.channel()
	channel.queue_declare(queue=queue)

	channel.basic_publish(exchange='', routing_key=queue, body=json.dumps(data))
	print(f"Data sent to RabbitMQ queue {queue}")
	connection.close()


# Function to send data to REST API
def send_to_rest_api(url, data):
	headers = {'Content-Type': 'application/json'}
	response = requests.post(url, json=data, headers=headers)

	if response.status_code == 200:
		print(f"Data sent to REST API: {response.json()}")
	else:
		print(f"Failed to send data to REST API: {response.status_code}")


# Main function to handle the sending logic
def send_data(service, config, data):
	if service == 'kafka':
		send_to_kafka(config['bootstrap_servers'], config['topic'], data)
	elif service == 'rabbitmq':
		send_to_rabbitmq(config['host'], config['queue'], data)
	elif service == 'restapi':
		send_to_rest_api(config['url'], data)
	else:
		print(f"Unsupported service: {service}")


# Example usage:
if __name__ == "__main__":
	main_data = {"key": "value"}

	# Kafka Example
	kafka_config = {
		"bootstrap_servers": ["localhost:9092"],
		"topic": "test_topic"
	}
	send_data("kafka", kafka_config, main_data)

	# RabbitMQ Example
	rabbitmq_config = {
		"host": "localhost",
		"queue": "test_queue"
	}
	send_data("rabbitmq", rabbitmq_config, main_data)

	# REST API Example
	restapi_config = {
		"url": "http://localhost:5000/api/data"
	}
	send_data("restapi", restapi_config, main_data)

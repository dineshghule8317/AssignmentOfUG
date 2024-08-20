import pika
import random
import time
import json
import paho.mqtt.client as mqtt

# Create MQTT client setup
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

mqtt_client.on_connect = on_connect
mqtt_client.connect("127.0.0.1", 1883, 60)

# Create RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='UpswingMessege')

while True:
    status = random.randint(0, 6)
    message = {
        "status": status,
        "timestamp": int(time.time())
    }
    # Publish to RabbitMQ
    channel.basic_publish(exchange='', routing_key='UpswingMessege', body=json.dumps(message))
    
    # Publish to MQTT Broker
    mqtt_client.publish("status/UpswingMessege", json.dumps(message))
    
    print(f"Sent: {message}")
    time.sleep(1)

connection.close()

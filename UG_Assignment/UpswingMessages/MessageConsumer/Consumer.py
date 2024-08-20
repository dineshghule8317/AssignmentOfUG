from django.core.management.base import BaseCommand
import pika
import json
from UpswingMessages.models import collection

class Command(BaseCommand):

    def handle(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='UpswingMessege')

        def callback(ch, method, properties, body):
            message = json.loads(body)
            collection.insert_one(message)
            print(f"Received and stored: {message}")

        channel.basic_consume(queue='UpswingMessege', on_message_callback=callback, auto_ack=True)
        print("Started consuming...")
        channel.start_consuming()

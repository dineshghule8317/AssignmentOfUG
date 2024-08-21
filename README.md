# MQTT Client-Server with RabbitMQ and Django

This project implements a client-server architecture where a Python client sends MQTT messages via RabbitMQ. 
The server, built with Django, processes these messages, stores them in MongoDB, and provides an API to query the data.

## Project Overview

- **Client**: Publishes MQTT messages to RabbitMQ. (messagePublisher.py)
- **Server**: Consumes messages from RabbitMQ, stores them in MongoDB, and exposes a REST API using Django.(UG_Assignment/UpswingMessages/MessageConsumer
/Consumer.py)

## Repository Structure

```plaintext
upswingGlobal/
│── upswingGlobal
|    └── ...               # Other app files (setting, models, views, urls, etc.)
├ UpswingMessages/
│   ├── UpswingMessages/          # Django settings and core files
│   ├── mqtt_app/             # Django app for handling MQTT messages
│   │   ├── messagesConsumer  /       # Custom management commands
│   │   │   └── consumer.py/     # for consume message and store
│   │   └── ...               # Other app files (models, views, urls, etc.)
│   ├── manage.py             # Django management script
│
├── messagePublisher.py       # Client script for publishing messages to RabbitMQ
├── requirements.txt          # Python dependencies
└── README.md                 # Project setup and operation instructions




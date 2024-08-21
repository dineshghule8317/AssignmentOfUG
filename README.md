# MQTT Client-Server with RabbitMQ and Django

This project implements a client-server architecture where a Python client sends MQTT messages via RabbitMQ. 
The server, built with Django, processes these messages, stores them in MongoDB, and provides an API to query the data.

## Project Overview

- **Client**: Publishes MQTT messages to RabbitMQ.
- **Server**: Consumes messages from RabbitMQ, stores them in MongoDB, and exposes a REST API.

## Repository Structure

```plaintext
upswingGlobal/
│── upswingGlobal
|    ├── manage.py             # Django management script
|    └── ...               # Other app files (setting, models, views, urls, etc.)
├ UpswingMessages/
│   ├── UpswingMessages/          # Django settings and core files
│   ├── mqtt_app/             # Django app for handling MQTT messages
│   │   ├── messagesConsumer  /       # Custom management commands
│   │   │   └── consumer.py/     # for consume message and store
│   │   └── ...               # Other app files (models, views, urls, etc.)
│  
│
├── messagePublisher.py       # Client script for publishing messages to RabbitMQ
├── requirements.txt          # Python dependencies
└── README.md                 # Project setup and operation instructions


import json
import argparse
import time
from confluent_kafka import Producer
import socket

# Función para enviar mensajes al topic de Kafka
def send_message(p, topic, key, value):
    p.produce(topic, key=key, value=value)
    time.sleep(1)  # Espera 1 segundo para simular el tiempo de procesamiento
    
producer = Producer({'bootstrap.servers': 'kafka1:9091,kafka2:9092'})
topic = 'big_data_topic'
key = 'data'
value = {
    'Mensaje': 'HOLA, ESTE ES UN MENSAJE DE PRUEBA',
    'Nombre': 'David',
    'Apellido': 'Medina',
    'Materia': 'Big Data',
    'Alumnos': [
        {
            'Nombre': 'Alex',
            'Apellido': 'Gonzalez',
            'Materia': 'Big Data'
        },
        {
            'Nombre': 'Marco',
            'Apellido': 'Gonzalez',
            'Materia': 'Big Data'
        },
        {
            'Nombre': 'Ana',
            'Apellido': 'Lopez',
            'Materia': 'Big Data'
        }
    ]
}

try:
    send_message(producer, topic, key, json.dumps(value).encode('utf-8'))
    producer.flush(30)
    print(f"Mensaje enviado: {value}")
except Exception as e:
    print(f"Error al enviar el mensaje: {e}")
finally:
    print("Esperando un nuevo texto...")
import json
from confluent_kafka import Consumer, KafkaException, KafkaError

# Configuración del consumidor
consumer_config = {
    'bootstrap.servers': 'kafka1:9091,kafka2:9092',
    'group.id': 'big_data_group',
    'auto.offset.reset': 'earliest'  # Comienza a leer desde el principio si no hay offset almacenado
}

# Crear el consumidor
consumer = Consumer(consumer_config)
topic = 'big_data_topic'

# Suscribirse al topic
consumer.subscribe([topic])

print(f"Esperando mensajes del topic '{topic}'...")

try:
    while True:
        # Leer mensajes del topic
        msg = consumer.poll(1.0)  # Espera 1 segundo por un mensaje

        if msg is None:
            continue  # No hay mensajes, continuar esperando
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # Fin de la partición
                print(f"Fin de la partición: {msg.topic()} [{msg.partition()}]")
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            # Mensaje recibido correctamente
            key = msg.key().decode('utf-8') if msg.key() else None
            value = json.loads(msg.value().decode('utf-8'))
            print(f"Mensaje recibido: Key={key}, Value={value}")

except KeyboardInterrupt:
    print("\nConsumo interrumpido por el usuario.")
finally:
    # Cerrar el consumidor
    consumer.close()
    print("Conexión cerrada.")
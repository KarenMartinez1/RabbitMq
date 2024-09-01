import pika
import json

def callback(ch, method, properties, body):
    mensaje_data = json.loads(body.decode())
    usuario = mensaje_data['usuario']
    mensaje = mensaje_data['mensaje']
    print(f" [*] {usuario}: {mensaje}")

def consumir_mensajes():
    # Establecer conexión con RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar la cola de mensajes
    channel.queue_declare(queue='mensajes')

    # Configurar el consumidor
    channel.basic_consume(queue='mensajes', on_message_callback=callback, auto_ack=True)
    print(' [*] Esperando mensajes. Para salir presiona CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consumir_mensajes()

import pika
import json
import time

def enviar_mensaje(usuario, mensaje):
    # Crear un diccionario con la información del mensaje
    mensaje_data = {
        'usuario': usuario,
        'mensaje': mensaje
    }
    # Convertir el diccionario a una cadena JSON
    mensaje_json = json.dumps(mensaje_data)

    # Establecer conexión con RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar la cola de mensajes
    channel.queue_declare(queue='mensajes')

    # Enviar el JSON como mensaje
    channel.basic_publish(exchange='', routing_key='mensajes', body=mensaje_json)
    print(f" [x] Enviado mensaje: {mensaje_data}")

    # Cerrar la conexión
    connection.close()

if __name__ == "__main__":
    # Ejemplo de envío de mensajes
    while True:
        usuario = input("Ingresa tu nombre de usuario: ")
        mensaje = input("Ingresa tu mensaje: ")
        enviar_mensaje(usuario, mensaje)
        time.sleep(1)  # Tiempo entre el envío de mensajes

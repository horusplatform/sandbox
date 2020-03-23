import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.31'))

channel = connection.channel()
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# severity 
severity = 'info'
channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

severity = 'error'
channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()

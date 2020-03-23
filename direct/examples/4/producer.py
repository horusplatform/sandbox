import pika
import json

from random import sample

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.31'))

channel = connection.channel()
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sample(['error', 'info', 'error', 'warning'], 1)[0]

payload = {
    'command' : 'hello',
    'severity' : severity
}

message = json.dumps(payload)
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
print(" [x] Sent %r:%r" % (severity, message))


import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.31'))

channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

payload = {
    'command' : 'hello'
}  

# using special exchange (empty string)
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=json.dumps(payload))

print(" [x] Sent 'Hello World!'")

connection.close()
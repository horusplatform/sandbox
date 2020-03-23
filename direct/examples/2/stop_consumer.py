import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.31'))
channel = connection.channel()

# create a queue 
queue = 'rtm_queue'

payload = {
    'command' : 'exit',
}

channel.queue_declare(queue=queue,durable=True)

# using special exchange (empty string)
channel.basic_publish(exchange='',
                      routing_key=queue,
                      body=json.dumps(payload),
                      properties=pika.BasicProperties (delivery_mode=2))   # message persistent

print(" [x] Sent payload message")

connection.close()
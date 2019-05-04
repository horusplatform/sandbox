import pika
import json
import random 

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.26'))

channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

for i in range(10):
    payload = json.dumps({'message' : f'Hello World {i}!',
                          'sleep' :  random.randint(0, 30)
    })    

    channel.basic_publish(exchange='', routing_key='task_queue',body=payload, properties=pika.BasicProperties(delivery_mode=2))

    print (f'[x] Sent {payload}')

connection.close()

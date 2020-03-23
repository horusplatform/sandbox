import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.queue_declare(queue='hello')

for i in range(10):
    #payload = {'message' : f'Hello World {i}!'}
    #payload =  f'Hello World {i}!'

    payload = json.dumps({'message' : f'Hello World {i}!'})    
    channel.basic_publish(exchange='', routing_key='hello',body=payload)

connection.close()

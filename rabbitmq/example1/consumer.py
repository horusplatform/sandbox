import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.31'))
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    #
    #print(" [x] Received %r" % body)

    payload = json.loads(body)
    print(json.dumps(payload, indent=4, sort_keys=True))

    #print (json.dumps(body))

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

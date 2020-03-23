import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.31'))
channel = connection.channel()

queue = 'rtm_queue'
channel.queue_declare(queue=queue)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
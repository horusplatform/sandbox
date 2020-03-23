import pika
import json
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.31'))
channel = connection.channel()

queue = 'rtm_queue'
#channel.queue_declare(queue=queue)

def callback(ch, method, properties, body):
    payload = json.loads(body)

    print(" [x] Received %r" % body)
 
    if (payload['command'] == 'sleep'):
        time.sleep(payload['timeout'])
        ch.basic_ack(delivery_tag = method.delivery_tag)

    elif (payload['command'] == 'exit'):
        ch.basic_ack(delivery_tag = method.delivery_tag)
        channel.stop_consuming()
    
    print('Done.')

channel.basic_qos(prefetch_count=1)   
channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
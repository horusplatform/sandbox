import pika
import json
import time


connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.26'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    payload = json.loads(body)

    print(f"[x] Received {payload}")
    time.sleep(payload['sleep'])        
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()

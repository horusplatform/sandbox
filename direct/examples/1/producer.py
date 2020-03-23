import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.31'))
channel = connection.channel()

# create a queue 
queue = 'rtm_queue'
payload = 'hello world'

channel.queue_declare(queue=queue)

# using special exchange (empty string)
channel.basic_publish(exchange='',
                      routing_key=queue,
                      body=payload)

print(" [x] Sent 'Hello World!'")

connection.close()
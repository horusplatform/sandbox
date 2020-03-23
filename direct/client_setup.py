import pika
import argparse

def init():
    parser = argparse.ArgumentParser(description='PyRTM Application')

    req = parser.add_argument_group('Required arguments')
    req.add_argument('--agent', type=int, metavar='<integer>', required=True, help='Agent ID attribute (rtm.agents.id)')

    opt = parser.add_argument_group('Optional arguments')    
    opt.add_argument('--rabbitmq-server', type=str, metavar='<string>', required=False, help='RabbitMQ server address', default='192.168.0.31')

    args = vars(parser.parse_args())

    return args

if __name__ == '__main__':
    args = init()

    connection = pika.BlockingConnection(pika.ConnectionParameters(args['rabbitmq_server']))
    channel = connection.channel()

    # exchanges
    channel.exchange_declare(exchange='direct.server.client', exchange_type='direct')
    channel.exchange_declare(exchange='direct.client.server', exchange_type='direct')

    # create unique queues 
    result = channel.queue_declare(queue='', durable=True)
    server_client_queue = result.method.queue

    result = channel.queue_declare(queue='', durable=True)
    client_server_queue = result.method.queue

    # bind queue
    channel.queue_bind(exchange='direct.server.client', queue=server_client_queue, routing_key=str(args['agent']))
    channel.queue_bind(exchange='direct.client.server', queue=client_server_queue, routing_key=str(args['agent']))

    # print result
    print(f'Server to client queue name : {server_client_queue}')
    print(f'Client to server queue name : {client_server_queue}')

import pika
import json
import argparse
import datetime

def init():
    parser = argparse.ArgumentParser(description='PyRTM Application')

    req = parser.add_argument_group('Required arguments')
    req.add_argument('--exchange', type=str, metavar='<str>', required=True, help='RabbitMQ exchange name')
    req.add_argument('--routing', type=str, metavar='<str>', required=True, help='Exchange routing key')

    opt = parser.add_argument_group('Optional arguments')    
    opt.add_argument('--rabbitmq-server', type=str, metavar='<string>', required=False, help='RabbitMQ server address', default='192.168.0.31')
    opt.add_argument('--callback', type=str, metavar='<string>', required=False, help='RabbitMQ callback exchange', default=None)

    args = vars(parser.parse_args())

    return args

def perform(server, routing, exchange, callback):
    connection = pika.BlockingConnection(pika.ConnectionParameters(server))
    channel = connection.channel()

    payload = {
        'server'    : server,
        'routing'   : routing,
        'callback'  : callback,
        'operation' : {
            'type'  : 'direct',
            'stdin' : 'print(1 + 2)'
        },
        'timestamp' : datetime.datetime.now().__str__()
    }
    
    message = json.dumps(payload)
    channel.basic_publish(exchange=exchange, routing_key=routing, body=message)

if __name__ == '__main__':
    args = init()

    perform(server=args['rabbitmq_server'], routing=args['routing'], exchange=args['exchange'], callback=args['callback'])
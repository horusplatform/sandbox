import pika
import json
import argparse
import producer 
import sys

from io import StringIO

from RestrictedPython import compile_restricted
from RestrictedPython import safe_builtins
from RestrictedPython import limited_builtins
from RestrictedPython import utility_builtins

def init():
    parser = argparse.ArgumentParser(description='PyRTM Application')

    req = parser.add_argument_group('Required arguments')
    req.add_argument('--queue', type=str, metavar='<str>', required=True, help='Agent queue name')

    opt = parser.add_argument_group('Optional arguments')    
    opt.add_argument('--rabbitmq-server', type=str, metavar='<string>', required=False, help='RabbitMQ server address', default='192.168.0.31')

    args = vars(parser.parse_args())

    return args


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag = method.delivery_tag)

    perform(ch, body)

def perform(channel, body):

    payload = json.loads(body)
    opcode = payload['operation']['type']

    if (opcode == 'direct'):
        command  = payload['operation']['stdin']
        callback = payload['callback']

        result = execute(command)
        print(result)

        if(callback):
            producer.perform(server=payload['server'], routing=payload['routing'], exchange=payload['callback'], callback=None)
            
    elif (opcode == 'shutdown'):
        channel.stop_consuming()


def execute(command):

    stdout = StringIO() 
    stderr = StringIO()

    source_code = f"""{command}"""

    sys.stdout = stdout
    sys.stderr = stderr

    try:
        byte_code = compile(source_code, filename='<inline code>',  mode='exec')
        exec(byte_code)

    except Exception as e:
        return {
            'stdout': None, 
            'stderr': e,
            'returnCode' : 255
        }

    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    return {
        'stdout': stdout.getvalue(), 
        'stderr': stderr.getvalue(),
        'returnCode' : 0
    }

if __name__ == '__main__':
    args = init()

    connection = pika.BlockingConnection(pika.ConnectionParameters(args['rabbitmq_server']))
    channel = connection.channel()

    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    channel.basic_consume(queue=args['queue'], on_message_callback=callback, auto_ack=False)
    channel.basic_qos(prefetch_count=1)
    channel.start_consuming()

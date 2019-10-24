#!/usr/bin/env python
import time
import pika
count = 0


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
channel.start_consuming()

print(' [*] Waiting for messages. To exit press CTRL+C')

#while True:
#    time.sleep(3)
#    print("hello world {count}".format(count=count))
#    count = count + 1
    
    




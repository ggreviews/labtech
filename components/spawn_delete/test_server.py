#!/usr/bin/env python
import subprocess
import psutil
import re
import pika
# https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)    

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

# proc = subprocess.Popen(['run_server.py',"param"], shell=True)
# proc = subprocess.run(['run_server.py',"param"], shell=True, stdout=None)
# try:
    # proc.wait(timeout=25)
# except subprocess.TimeoutExpired:
    # kill(proc.pid)

try:
    proc = subprocess.Popen(
        ['run_server.py',"param"], 
        shell=True,         
        encoding='utf-8',
        #stdout=subprocess.PIPE, 
        )
    channel.basic_publish(exchange='', routing_key='hello', body='Send Message NN')    
    channel.basic_publish(exchange='', routing_key='hello', body='Send Message NN')    
    channel.basic_publish(exchange='', routing_key='hello', body='Send Message NN')    
    connection.close()
# process stdout    
    print("processing stdout")
    stdout_str = proc.stdout
    #stdout_str = re.sub(' +', " ", stdout_str)
    #windlist = stdout_str.split('\n')
    #for line in range(len(windlist)):
    #    print(windlist[line].split(" ", 7))
    proc.wait(10)
    proc.terminate()
except subprocess.TimeoutExpired:
    print("subprocess terminated after t=10")

#!/usr/bin/env python
#https://medium.com/octopus-labs-london/how-to-build-a-rest-api-in-python-with-tornado-fc717c33824a

# to run webserver: pipenv run app.py
# visit: http://localhost:3000/

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import pymongo

class HelloHandler(RequestHandler):
  def get(self):
    self.write({'message': 'hello world'})

def make_app():
  urls = [("/", HelloHandler)]
  return Application(urls)
  
if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()    
    

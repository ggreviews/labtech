#!/usr/bin/env python

# To defend against XSRF and to add auth, consult with Security:
# https://www.tornadoweb.org/en/stable/guide/security.html

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json

items = []

class TodoItems(RequestHandler):
  def get(self):
    self.write({'items': items})


class TodoItem(RequestHandler):
  def post(self, _):
    items.append(json.loads(self.request.body))
    self.write({'message': 'new item added'})

  def delete(self, id):
    global items
    new_items = [item for item in items if item['id'] is not int(id)]
    items = new_items
    self.write({'message': 'Item with id %s was deleted' % id})
    
  def put(self, id):
    pass
    # Check that ID is not in use
    # Wire to mongo_db
  
  def get(self, id):
    pass
    

def make_app():
  urls = [
    ("/", TodoItems),
    (r"/api/item/([^/]+)?", TodoItem)
  ]
  app = Application(urls, debug=True)  
# only matches localhost or its ip address to prevent DNS Rebinding attack
# app.add_handlers(r'(localhost|127\.0\.0\.1)',urls)
  
  
if __name__ == '__main__':
  app = make_app()
  app.listen(3000)
  IOLoop.instance().start()
  
# def main():
    # app = make_app()
    # server = tornado.httpserver.HTTPServer(app)
    # server.bind(8888)
    # server.start(0)  # forks one process per cpu
    # IOLoop.current().start()        
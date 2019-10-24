#!/usr/bin/env python

# https://twistedmatrix.com/documents/12.0.0/core/howto/ssl.html
#https://www.digitalocean.com/community/tutorials/openssl-essentials-working-with-ssl-certificates-private-keys-and-csrs
#Generate a certificate from an existing private key:
#openssl req \
#       -key domain.key \
#       -new \
#       -x509 -days 365 -out domain.crt
# openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem

#bytes.decode() 
#str.encode(),

from OpenSSL import SSL
from twisted.internet import ssl, reactor
from twisted.internet.protocol import ClientFactory, Protocol

class EchoClient(Protocol):
    def connectionMade(self):
        print("hello, world")
        self.transport.write("hello, world!".encode())

    def dataReceived(self, data):
        print("Server said:", data)
        self.transport.loseConnection()

class EchoClientFactory(ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        reactor.stop()

class CtxFactory(ssl.ClientContextFactory):
    def getContext(self):
        self.method = SSL.SSLv23_METHOD
        ctx = ssl.ClientContextFactory.getContext(self)
        ctx.use_certificate_file('keys/client.crt')
        ctx.use_privatekey_file('keys/client.key')
        return ctx

if __name__ == '__main__':
    factory = EchoClientFactory()
    reactor.connectSSL('localhost', 8000, factory, CtxFactory())
    reactor.run()
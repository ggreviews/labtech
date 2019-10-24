#!/usr/bin/env python   

from OpenSSL import SSL
from twisted.internet import ssl, reactor
from twisted.internet.protocol import Factory, Protocol

class Echo(Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

def verifyCallback(connection, x509, errnum, errdepth, ok):
    if not ok:
        print('invalid cert from subject:', x509.get_subject())
        return False
    else:
        print("Certs are fine")
    return True

if __name__ == '__main__':
    factory = Factory()
    factory.protocol = Echo

    myContextFactory = ssl.DefaultOpenSSLContextFactory(
        'keys/server.key', 'keys/server.crt'
        )

    ctx = myContextFactory.getContext()

    ctx.set_verify(
        SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT,
        verifyCallback
        )

    # Since we have self-signed certs we have to explicitly
    # tell the server to trust them.
    ctx.load_verify_locations("keys/ca.pem")

    reactor.listenSSL(8000, factory, myContextFactory)
    reactor.run()
    
    
    
    
# from __future__ import print_function
# from twisted.protocols import basic

# class MyChat(basic.LineReceiver):
    # def connectionMade(self):
        # print("Got new client!")
        # self.factory.clients.append(self)

    # def connectionLost(self, reason):
        # print("Lost a client!")
        # self.factory.clients.remove(self)

    # def lineReceived(self, line):
        # print("received", repr(line))
        # for c in self.factory.clients:
            # c.message(line)

    # def message(self, message):
        # self.transport.write(message + b'\n')

# from twisted.internet import protocol
# from twisted.application import service, internet

# factory = protocol.ServerFactory()
# factory.protocol = MyChat
# factory.clients = []

# application = service.Application("chatserver")
# internet.TCPServer(1025, factory).setServiceParent(application)
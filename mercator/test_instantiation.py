import pytest
import mercator

def test_config_parser():
    conf = mercator.ConfigReader('config/laboratory.ini')
    assert conf.getKey('User',context='bitbucket.org') == 'hg', 'Test passed'
    
def test_rabbitmq_blackboard():
    uut = mercator.Blackboard()
    assert type(uut).__name__ == 'Blackboard'
    
def test_tornado_api():
    uut = mercator.RestServerFactory()
    assert type(uut).__name__ == 'RestServerFactory'
    
def test_ssl_chat():
    uut = mercator.SSLChat()
    assert type(uut).__name__ == 'SSLChat'

def test_mongo_adaptor():
    uut = mercator.MongoAdaptor()
    assert type(uut).__name__ == 'MongoAdaptor'

#
# CRUD Operations with Blackboard
#

def test_add_user_by_rabbitmq():
# Spawn blackboard server
# Run blackboard client
    uut = mercator.Blackboard()
    assert type(uut).__name__ == 'MongoAdaptor'


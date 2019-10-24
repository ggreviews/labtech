import configparser

class ConfigReader:

    def __init__(self,configfile):
        config = configparser.ConfigParser()
        config.read(configfile)
        self.config = config        
        
    def getKey(self,key,context='DEFAULT'):
        return self.config[context][key]
import configparser

config=configparser.RawConfigParser()
config.read("Configurations/config.ini")

class ReadConfig():
    @staticmethod
    def getBaseuRL():
        URL=config.get('common info','BASEURL')
        return URL

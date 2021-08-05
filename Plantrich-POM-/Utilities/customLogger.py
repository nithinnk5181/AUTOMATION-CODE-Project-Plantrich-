import logging
import unittest

class LogGen:
    @staticmethod
    def loggen():
        # Create and configure logger
        logging.basicConfig(filename="newfile.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
'''
class LogGen(unittest.TestCase):
    @staticmethod
    def loggen():
        #Create and configure logger
        logging.basicConfig(filename="newfile.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
'''

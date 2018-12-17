import os
import sys
import time
import datetime
import logging
import pandas as pd


logging.basicConfig(filename='class.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')

class Test(object):
    def __init__(self, spy=True):
        self.spy = spy

    def printf(self, *args, sep =' ', end='\n', file=None, std_out_print=True):
        #logging.debug('O método printf foi chamado em  ' +  ' ' +str(datetime.datetime.now()) )
        logging.debug('método chamado')
        logFile = open('log.txt', 'a')
        print(datetime.datetime.now(), end=' - ', file=logFile)
        print(*args, sep=sep, end=end, file=logFile)

        if (std_out_print):
            print(datetime.datetime.now(), end=' - ')
            print(*args, sep=sep, end=end)

        if (file is not None):
            print(datetime.datetime.now(), end=' - ', file=file)
            print(*args, sep=sep, end=end, file=file)


def getMean(methodName,log='class.log'):
    df = pd.read_csv('class.log')


if __name__ == "__main__":
    t = Test()
    t.printf('Estou testando esta funcao com um valore e ele é ',
             10, 12, sep='-', end='\n', file=open('log1.txt', 'a'))

    getMean('prinft')

    

import os, sys
import time
import datetime


'''
Funcao makeprint:
    Recebe dois argumentos ou mais
    String -> uma frase 
    Value - > um valor
    exemple makeprint('o valor passado é', 10)
            return irá printar em um arquivo logs.txt o datetime e timestamp e a frase "O valor passado é 10"
    caso você queira printar em mais de um arquivo 
            makeprint('o valor passado é',10, 'logs1.txt', 'logs2,txt') pode passar apenas logs1 também
            return irá printar em um arquivo logs.txt em logs1 e logs2.txt o datetime e timestamp e a frase "O valor passado é 10"
'''
def printf(*args, sep=' ', end='\n', file=None, std_out_print=True):
    logFile = open('log.txt', 'a')
    print(datetime.datetime.now(), end=' - ', file=logFile)
    print(*args, sep=sep, end=end, file=logFile)
    
    if (std_out_print):
        print(datetime.datetime.now(), end=' - ')
        print(*args, sep=sep, end=end)
    
    if (file is not None):
        print(datetime.datetime.now(), end=' - ', file=file)
        print(*args, sep=sep, end=end, file=file)


printf('Estou testando esta funcao com um valore e ele é ', 10, 12, sep='-', end='\n', file=open('log1.txt', 'a'))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


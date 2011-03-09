'''
Created on 24/feb/2011

@author: A144220
'''
import random

class SuperEnalotto():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def calculate(self):

        sacco = []
        serie = []
        for i in range(1,91):
            sacco.append(i)
        
        random.shuffle(sacco)
        
        for i in range(0, 6):
            indice = random.randint(0,89)
            if sacco[indice] <> '':
                serie.append(sacco[indice])
                sacco[indice] = ''
        
        serie.sort()
        return serie

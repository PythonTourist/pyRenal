import random

class Win4Life(object):
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
        for i in range(1,21):
            sacco.append(i)
        random.shuffle(sacco)
        
        i = 0
        while i < 10:
            indice = random.randint(0,19)
            if sacco[indice] <> '':
                serie.append(sacco[indice])
                sacco[indice] = ''
                random.shuffle(sacco)
                i = i+1
        
        serie.sort()
        return serie
    
if __name__ == "__main__":
    a = Win4Life()
    s = a.calculate()
    print str(s)

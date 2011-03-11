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
        
        i = 0
        while i < 6:
            indice = random.randint(0,89)
            if sacco[indice] <> '':
                serie.append(sacco[indice])
                sacco[indice] = ''
                i = i+1
        
        serie.sort()
        return serie

if __name__ == "__main__":
    a = SuperEnalotto()
    s = a.calculate()
    print str(s)
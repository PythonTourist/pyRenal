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
# This will simulate a sack with the 90 numbers in. This is not necessary for random number extraction,
# is just a mode to intend it.
        for i in range(1,91):
            sacco.append(i)
# The sack is shuffled        
        random.shuffle(sacco)
        
        i = 0
        while i < 6:
# The number is randomly extracted from the sack
            indice = random.randint(0,89)
# Check if the position is already extracted
            if sacco[indice] <> '':
# Add the number extracted at the dated position in the serie
                serie.append(sacco[indice])
# Delete the number at the position
                sacco[indice] = ''
# The sack is shuffled again at every extraction                
                random.shuffle(sacco)
                i = i+1
 # Sort the serie       
        serie.sort()
        return serie

if __name__ == "__main__":
    a = SuperEnalotto()
    s = a.calculate()
    print str(s)

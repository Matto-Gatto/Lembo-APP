from Squadra import *
from Partita import *

def Ex6(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex6, ['partite1.csv'],[Partita(Squadra('Argentina'),Squadra('Francia'),7,5),Partita(Squadra('Croazia'),Squadra('Marocco'),2,1),Partita(Squadra('Francia'),Squadra('Marocco'),2,0),Partita(Squadra('Argentina'),Squadra('Croazia'),3,0)])
    counter_test_positivi += tester_fun(Ex6, ['partite2.csv'],[Partita(Squadra('Juventus'),Squadra('Venezia'),2,2)])
    counter_test_positivi += tester_fun(Ex6, ['partite3.csv'],[])
    counter_test_positivi += tester_fun(Ex6, ['partite4.csv'],[Partita(Squadra('Scapoli'),Squadra('Ammogliati'),5,5),Partita(Squadra('TerzaB'),Squadra('TerzaC'),0,0)]) 
    counter_test_positivi += tester_fun(Ex6, ['partite5.csv'],[Partita(Squadra('Italia'),Squadra('Germania'),2,0), \
                                                               Partita(Squadra('Italia'),Squadra('Francia'),5,3), \
                                                               Partita(Squadra('Portogallo'),Squadra('Francia'),0,1), \
                                                               Partita(Squadra('Brasile'),Squadra('Francia'),0,1), \
                                                               Partita(Squadra('Italia'),Squadra('Ucraina'),3,0), \
                                                               Partita(Squadra('Germania'),Squadra('Argentina'),4,2)])     

    print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

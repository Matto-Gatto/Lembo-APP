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

    counter_test_positivi += tester_fun(Ex6, ['partite1.csv'],{Squadra('Argentina')})
    counter_test_positivi += tester_fun(Ex6, ['partite2.csv'],{Squadra('Juventus'),Squadra('Venezia')})
    counter_test_positivi += tester_fun(Ex6, ['partite3.csv'],set())
    counter_test_positivi += tester_fun(Ex6, ['partite4.csv'],{Squadra('TerzaC'), Squadra('Ammogliati'), Squadra('Scapoli'), Squadra('TerzaB')}) 
    counter_test_positivi += tester_fun(Ex6, ['partite5.csv'],{Squadra('Italia')})     

    print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

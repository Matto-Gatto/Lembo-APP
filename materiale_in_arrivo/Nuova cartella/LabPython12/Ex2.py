from Tempo import *

def Ex2(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, [[Tempo(10,15),Tempo(9,12,34),Tempo(8,30,2)]], [Tempo(8,30,2),Tempo(9,12,34),Tempo(10,15)])
    counter_test_positivi += tester_fun(Ex2, [[Tempo(12,10)]], [Tempo(12,10)])
    counter_test_positivi += tester_fun(Ex2, [[Tempo(18,15),Tempo(9,11,30),Tempo(18,15)]], [Tempo(9,11,30),Tempo(18,15)])
    counter_test_positivi += tester_fun(Ex2, [[Tempo(18,15),Tempo(),Tempo(Ore=12),Tempo(18,15,0)]], [Tempo(),Tempo(Ore=12),Tempo(18,15)])
    counter_test_positivi += tester_fun(Ex2, [[Tempo(),Tempo(0,0,0),Tempo(Secondi=0)]], [Tempo()])
    

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

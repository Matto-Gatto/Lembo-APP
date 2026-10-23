from Tempo import *

def Ex3(t,s):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, [Tempo(10,15),30], Tempo(10,15,30))
    counter_test_positivi += tester_fun(Ex3, [Tempo(10,15),75], Tempo(10,16,15))
    counter_test_positivi += tester_fun(Ex3, [Tempo(10,15),3675], Tempo(11,16,15))
    counter_test_positivi += tester_fun(Ex3, [Tempo(23,15),3675], Tempo(0,16,15))
    counter_test_positivi += tester_fun(Ex3, [Tempo(20,10,12),18600], Tempo(1,20,12))
    

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

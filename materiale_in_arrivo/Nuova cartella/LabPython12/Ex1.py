from Tempo import *

def Ex1(t1,t2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, [Tempo(11,10),Tempo(9,30,15)], 5985)
    counter_test_positivi += tester_fun(Ex1, [Tempo(9,30,15),Tempo(11,10)], 5985)
    counter_test_positivi += tester_fun(Ex1, [Tempo(10,15),Tempo(9,12,34)], 3746)
    counter_test_positivi += tester_fun(Ex1, [Tempo(12,10),Tempo(12,10)], 0)
    counter_test_positivi += tester_fun(Ex1, [Tempo(),Tempo(Minuti=50)],3000)
    

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

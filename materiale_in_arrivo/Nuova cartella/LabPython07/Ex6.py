def Ex6(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex6, [[3,7,8,9]], 'DDPD')
    counter_test_positivi += tester_fun(Ex6, [[3]], 'D')
    counter_test_positivi += tester_fun(Ex6, [[8]], 'P')
    counter_test_positivi += tester_fun(Ex6, [[]], '')
    counter_test_positivi += tester_fun(Ex6, [[7,7,7,7,8]], 'DDDDP')

    print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

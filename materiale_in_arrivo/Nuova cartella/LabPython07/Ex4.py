def Ex4(start,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex4, [4,3], [4,5,6])
    counter_test_positivi += tester_fun(Ex4, [-15,3], [-15,-14,-13])
    counter_test_positivi += tester_fun(Ex4, [15,0], [])
    counter_test_positivi += tester_fun(Ex4, [0,3], [0,1,2])
    counter_test_positivi += tester_fun(Ex4, [201,1], [201])

    print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

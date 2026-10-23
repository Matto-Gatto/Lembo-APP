def Ex8(l1, l2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, [[1, 3, 2, 1, -5],[1, 3]],[-5, 2])
    counter_test_positivi += tester_fun(Ex8, [[1, 3, 2, 1, -5],[1, 1, 1]],[-5, 2, 3])
    counter_test_positivi += tester_fun(Ex8, [[10, 1, 10, 1, 2],[10, 1, 2]],[])
    counter_test_positivi += tester_fun(Ex8, [[],[1, 1, 1]],[])
    counter_test_positivi += tester_fun(Ex8, [[100, 12, -2, -1, -2],[]],[-2, -2, -1, 12, 100])

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

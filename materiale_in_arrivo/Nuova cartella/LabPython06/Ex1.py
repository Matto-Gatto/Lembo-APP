def Ex1(s,c):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, ['AzzuRRO','a'],3)
    counter_test_positivi += tester_fun(Ex1, ['AzzuRRO','A'],6)
    counter_test_positivi += tester_fun(Ex1, ['Albergo','b'],5)
    counter_test_positivi += tester_fun(Ex1, ['Roma','Z'],3)
    counter_test_positivi += tester_fun(Ex1, ['barca','s'],0)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

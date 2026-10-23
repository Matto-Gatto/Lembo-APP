def Ex7(s):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun
    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex7, ['aHa^^&^HH'], 3)
    counter_test_positivi += tester_fun(Ex7, [''], 0)
    counter_test_positivi += tester_fun(Ex7, ['&&YH&Y'], 2)
    counter_test_positivi += tester_fun(Ex7, ['stri%$p'], 0)
    counter_test_positivi += tester_fun(Ex7, ['CIAO'], 1)

    counter_test_positivi += tester_fun(Ex7, ['s/NN//^/^^NNCC'], 4)
    counter_test_positivi += tester_fun(Ex7, ['&&OF&O'], 2)
    counter_test_positivi += tester_fun(Ex7, ['xfl&%pl'], 0)
    counter_test_positivi += tester_fun(Ex7, ['H 112 BB CCCC EEE'], 4)
    counter_test_positivi += tester_fun(Ex7, ['HELO'], 1)

    print('La funzione',Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

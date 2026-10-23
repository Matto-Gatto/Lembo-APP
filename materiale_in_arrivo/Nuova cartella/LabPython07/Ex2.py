def Ex2(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
if __name__ == '__main__':
    from tester import tester_fun
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, [['tanto','va','la','gatta','al','lardo']], 5)
    counter_test_positivi += tester_fun(Ex2, [['ciao','mamma','guarda','come','sono','bravo']], 6)
    counter_test_positivi += tester_fun(Ex2, [['','pippo']], 5)
    counter_test_positivi += tester_fun(Ex2, [['supercalifragilistichespiralidoso']], 33)
    counter_test_positivi += tester_fun(Ex2, [['a','b','c','d']], 1)


    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

def Ex1(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
if __name__ == '__main__':
    from tester import tester_fun
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, [['tanto','va','la','gatta','al','lardo']], [5,2,2,5,2,5])
    counter_test_positivi += tester_fun(Ex1, [['ciao','mamma','guarda','come','sono','bravo']], [4,5,6,4,4,5])
    counter_test_positivi += tester_fun(Ex1, [['','pippo']], [0,5])
    counter_test_positivi += tester_fun(Ex1, [['supercalifragilistichespiralidoso']], [33])
    counter_test_positivi += tester_fun(Ex1, [['a','b','c','d']], [1,1,1,1])


    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

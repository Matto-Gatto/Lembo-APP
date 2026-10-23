def Ex3(n,m):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
	
	
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun
    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, [3,11], 63)
    counter_test_positivi += tester_fun(Ex3, [3,-2], 0)
    counter_test_positivi += tester_fun(Ex3, [3,3], 3)
    counter_test_positivi += tester_fun(Ex3, [8,10], 27)
    counter_test_positivi += tester_fun(Ex3, [-3,-2], -5)
    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


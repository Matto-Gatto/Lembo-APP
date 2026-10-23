def Ex9(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex9, ['quadrato1.txt'] , True)
    counter_test_positivi += tester_fun(Ex9, ['quadrato2.txt'] , False)
    counter_test_positivi += tester_fun(Ex9, ['quadrato3.txt'] , False)
    counter_test_positivi += tester_fun(Ex9, ['quadrato4.txt'] , True)
    counter_test_positivi += tester_fun(Ex9, ['quadrato5.txt'] , False)

    print('La funzione',Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

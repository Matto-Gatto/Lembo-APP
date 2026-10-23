def Ex3(l1, l2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
if __name__ == '__main__':
    from tester import tester_fun
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, [[3,6],[3,4,9]] , [6, 10, 9])
    counter_test_positivi += tester_fun(Ex3, [[],[3,4,9]] , [3, 4, 9])
    counter_test_positivi += tester_fun(Ex3, [[3,6],[3,4]] ,[6, 10])
    counter_test_positivi += tester_fun(Ex3, [[1],[9]] ,[10])
    counter_test_positivi += tester_fun(Ex3, [[],[9]] ,[9])


    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

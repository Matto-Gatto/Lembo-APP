def Ex4(n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""


if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex4, [3] , {0:0,1:1,2:4,3:9})
    counter_test_positivi += tester_fun(Ex4, [0] , {0:0})
    counter_test_positivi += tester_fun(Ex4, [2] , {0:0,1:1,2:4})
    counter_test_positivi += tester_fun(Ex4, [4] , {0:0,1:1,2:4,3:9,4:16})
    counter_test_positivi += tester_fun(Ex4, [10], {0:0,1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100})

    print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

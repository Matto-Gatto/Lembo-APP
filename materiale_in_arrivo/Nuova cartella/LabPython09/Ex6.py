def Ex6(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex6, ["testo_1.txt"] , {1: 10})
    counter_test_positivi += tester_fun(Ex6, ["testo_2.txt"] , {1: 7})
    counter_test_positivi += tester_fun(Ex6, ["testo_3.txt"] , {1: 8, 2: 7, 3: 7})
    counter_test_positivi += tester_fun(Ex6, ["testo_4.txt"] , {1: 8, 2: 7, 3: 7, 4: 7})
    counter_test_positivi += tester_fun(Ex6, ["testo_5.txt"] , {1: 1, 2: 1, 3: 1, 4: 1})

    print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

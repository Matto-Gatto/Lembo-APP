def Ex5(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex5, ["testo_1.txt"] , {1: 45})
    counter_test_positivi += tester_fun(Ex5, ["testo_2.txt"] , {1: 38})
    counter_test_positivi += tester_fun(Ex5, ["testo_3.txt"] , {1: 27, 2: 19, 3: 13})
    counter_test_positivi += tester_fun(Ex5, ["testo_4.txt"] , {1: 27, 2: 26, 3: 26, 4: 23})
    counter_test_positivi += tester_fun(Ex5, ["testo_5.txt"] , {1: 4, 2: 4, 3: 4, 4: 1})

    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

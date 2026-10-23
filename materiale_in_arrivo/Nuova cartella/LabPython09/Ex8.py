def Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["testo_1.txt"] , 1)
    counter_test_positivi += tester_fun(Ex8, ["testo_2.txt"] , 3)
    counter_test_positivi += tester_fun(Ex8, ["testo_3.txt"] , 3)
    counter_test_positivi += tester_fun(Ex8, ["testo_4.txt"] , 5)
    counter_test_positivi += tester_fun(Ex8, ["testo_5.txt"] , 0)

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

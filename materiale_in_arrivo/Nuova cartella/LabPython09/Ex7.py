def Ex7(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex7, ["testo_1.txt"] , {1: 'A'})
    counter_test_positivi += tester_fun(Ex7, ["testo_2.txt"] , {1: 'a'})
    counter_test_positivi += tester_fun(Ex7, ["testo_3.txt"] , {1: 'S', 2:'A', 3:'a' })
    counter_test_positivi += tester_fun(Ex7, ["testo_4.txt"] , {1: 'P', 2: 'A', 3: 'a', 4: 'a'})
    counter_test_positivi += tester_fun(Ex7, ["testo_5.txt"] , {1: 'a', 2: 'a', 3: 'a', 4: 'a'})

    print('La funzione',Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

def Ex5(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex5, ["ip1.txt"] , {'invalidi': 3, 'domestici': 1, 'altri': 1})
    counter_test_positivi += tester_fun(Ex5, ["ip2.txt"] , {'invalidi': 0, 'domestici': 0, 'altri': 5})
    counter_test_positivi += tester_fun(Ex5, ["ip3.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex5, ["ip4.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex5, ["ip5.txt"] , {'invalidi': 2, 'domestici': 1, 'altri': 2})

    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

from tester import tester_fun

def B_Ex2(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, ['file1.txt'],{'I': [1], 'A': [1], 'e': [1], 'u': [2, 3]})
counter_test_positivi += tester_fun(B_Ex2, ['file2.txt'],{'I': [1], 'A': [1], 'e': [1, 5], 'u': [2, 3, 5, 6], 'o': [4, 5]} )
counter_test_positivi += tester_fun(B_Ex2, ['file3.txt'],{'I': [1], 'A': [1], 'u': [1, 2, 3]})
counter_test_positivi += tester_fun(B_Ex2, ['file4.txt'],{'I': [1], 'A': [1, 4], 'u': [1, 2, 3, 4, 6], 'o': [5], 'e': [6]} )
counter_test_positivi += tester_fun(B_Ex2, ['file5.txt'],{'I': [1, 7, 8], 'A': [1, 4], 'u': [1, 2, 3, 4, 6, 8, 9], 'o': [5], 'e': [6]})

print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


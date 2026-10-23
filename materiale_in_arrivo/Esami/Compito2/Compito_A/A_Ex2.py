from tester import tester_fun

def A_Ex2(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
                          
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, ['file1.txt'],{'c': [1], 'z': [1], 'n': [2, 3]}  )
counter_test_positivi += tester_fun(A_Ex2, ['file2.txt'],{'c': [1, 5], 'z': [1], 'n': [2, 5], 't': [3, 6], 'l': [4], 's': [4], 'r': [5], 'v': [5], 'd': [5]} )
counter_test_positivi += tester_fun(A_Ex2, ['file3.txt'], {'n': [1], 'l': [2], 't': [3]})
counter_test_positivi += tester_fun(A_Ex2, ['file4.txt'],{'n': [1, 4, 5], 'l': [2, 5, 6], 't': [3], 'p': [5], 'z': [6]} )
counter_test_positivi += tester_fun(A_Ex2, ['file5.txt'],{'n': [1, 4, 5], 'l': [2, 5, 6, 8, 9], 't': [3, 7], 'p': [5], 'z': [6]})

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

from tester import tester_fun

def A_Ex2(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
                                
###############################################################################


"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, ['file1.txt'],'albero')
counter_test_positivi += tester_fun(A_Ex2, ['file2.txt'],'giovane')
counter_test_positivi += tester_fun(A_Ex2, ['file3.txt'],'casolare')
counter_test_positivi += tester_fun(A_Ex2, ['file4.txt'],'giovane')
counter_test_positivi += tester_fun(A_Ex2, ['file5.txt'],'')

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

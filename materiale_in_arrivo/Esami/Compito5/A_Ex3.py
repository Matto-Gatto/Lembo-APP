from tester import tester_fun

def A_Ex3(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ['performance1.csv'],{12: [27, 20, 10, 36]})
counter_test_positivi += tester_fun(A_Ex3, ['performance2.csv'],{12: [27, 20, 10, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex3, ['performance3.csv'],{12: [37, 50, 10, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex3, ['performance4.csv'],{12: [49, 50, 34, 36], 10: [37, 20, 24, 45]})
counter_test_positivi += tester_fun(A_Ex3, ['performance5.csv'],{12: [69, 110, 34, 36], 10: [37, 20, 24, 45]})



print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

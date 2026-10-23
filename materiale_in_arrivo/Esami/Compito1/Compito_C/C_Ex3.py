from tester import tester_fun

def C_Ex3(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex3, ['comande1.csv'],{1:9, 2:6})
counter_test_positivi += tester_fun(C_Ex3, ['comande2.csv'],{1:23, 2:6})
counter_test_positivi += tester_fun(C_Ex3, ['comande3.csv'],{1:23, 2:6, 3:2})
counter_test_positivi += tester_fun(C_Ex3, ['comande4.csv'],{1: 23, 2: 11, 3: 14})
counter_test_positivi += tester_fun(C_Ex3, ['comande5.csv'],{1: 23, 2: 11, 3: 14, 4: 17})

print('La funzione',C_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

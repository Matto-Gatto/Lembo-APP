from tester import tester_fun

def A_Ex3(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
            
                
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ['maratone1.csv'],{'Mario': [130, 3, 0, 1], 'Paolo': [132, 2, 1, 1], 'Gianna': [130, 1, 1, 0], 'Giulia': [121, 2, 1, 1]})
counter_test_positivi += tester_fun(A_Ex3, ['maratone2.csv'],{'Mario': [111, 3, 1, 0], 'Paolo': [112, 3, 1, 1], 'Gianna': [113, 2, 1, 0], 'Giulia': [114, 3, 1, 1], 'Riccardo': [115, 2, 0, 2]})
counter_test_positivi += tester_fun(A_Ex3, ['maratone3.csv'],{'Mario': [135, 2, 0, 0], 'Paolo': [132, 2, 1, 1], 'Gianna': [130, 1, 1, 0], 'Giulia': [121, 2, 1, 1], 'Riccardo': [132, 1, 0, 1]})
counter_test_positivi += tester_fun(A_Ex3, ['maratone4.csv'],{'Mario': [121, 4, 1, 0], 'Paolo': [132, 3, 1, 2], 'Gianna': [122, 2, 1, 0], 'Giulia': [121, 3, 1, 1], 'Riccardo': [132, 1, 0, 0], 'Melania': [124, 3, 1, 2]})
counter_test_positivi += tester_fun(A_Ex3, ['maratone5.csv'],{'Mario': [121, 4, 2, 0], 'Paolo': [132, 3, 1, 2], 'Gianna': [122, 2, 1, 0], 'Giulia': [121, 3, 1, 2], 'Riccardo': [132, 1, 0, 1]})

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

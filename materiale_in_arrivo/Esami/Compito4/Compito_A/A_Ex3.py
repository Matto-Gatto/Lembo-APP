from tester import tester_fun

def A_Ex3(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
             

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ['performance1.csv'],{'Mario': [1, 2], 'Marco': [], 'Anna': [3,4], 'Aldo': [2], 'Antonio': [5]})
counter_test_positivi += tester_fun(A_Ex3, ['performance2.csv'],{'Mario': [2], 'Marco': [], 'Anna': [1,3,4], 'Aldo':[], 'Antonio':[5]})
counter_test_positivi += tester_fun(A_Ex3, ['performance3.csv'],{'Mario': [], 'Marco': [], 'Anna': [1,2,3,4,5], 'Antonio':[]})
counter_test_positivi += tester_fun(A_Ex3, ['performance4.csv'],{'Mario': [1,4], 'Anna': [2,3,5]})
counter_test_positivi += tester_fun(A_Ex3, ['performance5.csv'],{'Mario': [1,2,4], 'Marco': [1,4], 'Anna': [1,3,4,5], 'Aldo': [2,3], 'Antonio': [5]})



print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

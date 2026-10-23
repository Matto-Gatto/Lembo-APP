from tester import tester_fun

def A_Ex3(file,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""          

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ['voli1.csv',3],['Londra','Parigi'])
counter_test_positivi += tester_fun(A_Ex3, ['voli1.csv',5],['Parigi'])
counter_test_positivi += tester_fun(A_Ex3, ['voli2.csv',4],['Londra', 'Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(A_Ex3, ['voli2.csv',7],['Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(A_Ex3, ['voli2.csv',11],[])

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

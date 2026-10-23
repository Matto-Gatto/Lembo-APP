from tester import tester_fun

def B_Ex3(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, ['voli1.csv'],['Londra','Parigi'])
counter_test_positivi += tester_fun(B_Ex3, ['voli2.csv'],['Londra', 'Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(B_Ex3, ['voli3.csv'],['Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(B_Ex3, ['voli4.csv'],['Parigi'])
counter_test_positivi += tester_fun(B_Ex3, ['voli5.csv'],[])

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

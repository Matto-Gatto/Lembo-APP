from tester import tester_fun

def Ex3(file):
    """Inserite qui la vostra soluzione"""
   

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex3, ['ruota1.csv'],[14,50])
counter_test_positivi += tester_fun(Ex3, ['ruota2.csv'],[2,14])
counter_test_positivi += tester_fun(Ex3, ['ruota3.csv'],[2])
counter_test_positivi += tester_fun(Ex3, ['ruota4.csv'],[24,43,47,50])
counter_test_positivi += tester_fun(Ex3, ['ruota5.csv'],[])

print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

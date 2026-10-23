from tester import tester_fun

def A_Ex1(s,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
     
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ["ossessivo",4],1)
counter_test_positivi += tester_fun(A_Ex1, ["Anna",2],2)
counter_test_positivi += tester_fun(A_Ex1, ["amico",1],5)
counter_test_positivi += tester_fun(A_Ex1, ["allenAtrice",2],3)
counter_test_positivi += tester_fun(A_Ex1, ["pippo",3],1)

print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

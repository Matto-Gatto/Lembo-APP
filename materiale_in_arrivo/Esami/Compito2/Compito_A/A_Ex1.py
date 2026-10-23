from tester import tester_fun

def A_Ex1(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, [["mamma","sola","casa"]],["a", "c", "m", "o", "s"])
counter_test_positivi += tester_fun(A_Ex1, [["mamma","sole","casa","sacco"]],["a", "c", "e", "m", "o", "s"])
counter_test_positivi += tester_fun(A_Ex1, [["pippo","castello","se"]],["a","l","o","p","s","t"])
counter_test_positivi += tester_fun(A_Ex1, [[]],[])
counter_test_positivi += tester_fun(A_Ex1, [["assolo",""]],["a","l","s"])


print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

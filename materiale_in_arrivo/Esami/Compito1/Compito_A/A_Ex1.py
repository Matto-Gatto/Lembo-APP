from tester import tester_fun

def A_Ex1(s1, s2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ["amaca","amato"],"ama")
counter_test_positivi += tester_fun(A_Ex1, ["pippo","minnie"], "")
counter_test_positivi += tester_fun(A_Ex1, ["","pippo"], "")
counter_test_positivi += tester_fun(A_Ex1, ["arte","arteria"] ,"arte")
counter_test_positivi += tester_fun(A_Ex1, ["amato","ama"] ,"ama")

print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


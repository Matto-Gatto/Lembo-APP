from tester import tester_fun

def D_Ex2(l1,l2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(D_Ex2, [["mamma", "asso", "re"],["amamm", "lago", "er"]],["mamma", "re"])
counter_test_positivi += tester_fun(D_Ex2, [["sara","osso"],["asar","ooss"]],["osso","sara"])
counter_test_positivi += tester_fun(D_Ex2, [["sara"],["rasa"]],[])
counter_test_positivi += tester_fun(D_Ex2, [["a"],["a"]],["a"])
counter_test_positivi += tester_fun(D_Ex2, [["a"],["A"]],[])

print('La funzione',D_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

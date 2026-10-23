from tester import tester_fun

def B_Ex1(s1,s2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex1, ["arciere","pompiere"], 4)
counter_test_positivi += tester_fun(B_Ex1, ["arciere","pippo"], 0)
counter_test_positivi += tester_fun(B_Ex1, ["","pompiere"] , 0)
counter_test_positivi += tester_fun(B_Ex1, ["ma","mamma"] , 2)
counter_test_positivi += tester_fun(B_Ex1, ["reggimento","mento"] , 5)

print('La funzione',B_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

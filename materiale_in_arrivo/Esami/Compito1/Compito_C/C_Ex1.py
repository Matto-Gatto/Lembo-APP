from tester import tester_fun

def C_Ex1(s1, s2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5 

counter_test_positivi += tester_fun(C_Ex1, ["abcd","xyefgh"] , "ahbgcfdexy")
counter_test_positivi += tester_fun(C_Ex1, ["abcd","ef"] , "afbecd")
counter_test_positivi += tester_fun(C_Ex1, ["abc","abc"] , "acbbca")
counter_test_positivi += tester_fun(C_Ex1, ["xyz","a"] , "xayz")
counter_test_positivi += tester_fun(C_Ex1, ["a","b"] , "ab")

print('La funzione',C_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

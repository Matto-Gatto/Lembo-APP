def Ex10(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex10, [[{3,2,90},{2,87,23},{2,23,3}]] , {90,87})
    counter_test_positivi += tester_fun(Ex10, [[set(),{-10},{2}]] , {-10,2})
    counter_test_positivi += tester_fun(Ex10, [[{1},{1},{1}]] , set())
    counter_test_positivi += tester_fun(Ex10, [[set(),{10,-2},{10},{-2}]] , set())
    counter_test_positivi += tester_fun(Ex10, [[set(),{10,-9,4},{4,-5,2},{3,7,4}]] , {10,-9,-5,2,3,7})

    counter_test_positivi += tester_fun(Ex10, [[{10}]] , {10})
    counter_test_positivi += tester_fun(Ex10, [[{10,2}]] , {10,2})
    counter_test_positivi += tester_fun(Ex10, [[{10,2},{10}]] , {2})
    counter_test_positivi += tester_fun(Ex10, [[set()]] , set())
    counter_test_positivi += tester_fun(Ex10, [[{6},{1},{1,2,3,4,5,6}]] , {2,3,4,5})


    print('La funzione',Ex10.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

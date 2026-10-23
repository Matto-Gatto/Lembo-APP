def Ex4(i):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex4, [{3,345,15,24,25,-10}], [-10,15,25,345])
    counter_test_positivi += tester_fun(Ex4, [set()], [])
    counter_test_positivi += tester_fun(Ex4, [{1,2,3}], [])
    counter_test_positivi += tester_fun(Ex4, [{5,10,0,-5,-10}], [-10,-5,0,5,10])
    counter_test_positivi += tester_fun(Ex4, [{100,50,-12,34,65}], [50,65,100])

    counter_test_positivi += tester_fun(Ex4, [{6,10,8}], [10])
    counter_test_positivi += tester_fun(Ex4, [{-5,-4,-3,-2,-1,0}], [-5,0])
    counter_test_positivi += tester_fun(Ex4, [{6,7,8}], [])
    counter_test_positivi += tester_fun(Ex4, [{55}], [55])
    counter_test_positivi += tester_fun(Ex4, [{135,875,-500}], [-500,135,875])

    print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

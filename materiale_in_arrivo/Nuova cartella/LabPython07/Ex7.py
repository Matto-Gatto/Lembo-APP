def Ex7(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex7, [["ama","ma","amaca"]], [303,206,499])
    counter_test_positivi += tester_fun(Ex7, [[]], [])
    counter_test_positivi += tester_fun(Ex7, [["c"]], [99])
    counter_test_positivi += tester_fun(Ex7, [["ciao",""]], [412,0])
    counter_test_positivi += tester_fun(Ex7, [["",""]], [0,0])

    print('La funzione',Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

def Ex10(s1,s2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex10, ['amaca','amaranto'], 'ama')
    counter_test_positivi += tester_fun(Ex10, ['asso','assolato'], 'asso')
    counter_test_positivi += tester_fun(Ex10, ['','stringa'], '')
    counter_test_positivi += tester_fun(Ex10, ['stringa',''], '')
    counter_test_positivi += tester_fun(Ex10, ['ciao mamma','ciao '], 'ciao ')

    print('La funzione',Ex10.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

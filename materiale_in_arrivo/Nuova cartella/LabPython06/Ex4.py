def Ex4(s1,s2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex4, ['pippo','zorro'] ,'pizr')
    counter_test_positivi += tester_fun(Ex4, ['pippo','pluto'] ,'ilut')
    counter_test_positivi += tester_fun(Ex4, ['ciao','mamma'] ,'ciom')
    counter_test_positivi += tester_fun(Ex4, ['ciao',''] ,'ciao')
    counter_test_positivi += tester_fun(Ex4, ['','osso'] ,'os')

    print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

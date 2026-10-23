def Ex9(s):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex9, ['cIAo MAmMa'],['A','I','M'])
    counter_test_positivi += tester_fun(Ex9, ['3219'], [])
    counter_test_positivi += tester_fun(Ex9, ['aG2Hl'], ['G','H'])
    counter_test_positivi += tester_fun(Ex9, ['PPq&/&90PQ'], ['P','Q'])
    counter_test_positivi += tester_fun(Ex9, [''], [])

    print('La funzione',Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

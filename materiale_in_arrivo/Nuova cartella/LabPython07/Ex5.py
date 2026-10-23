def Ex5(l,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex5, [['tanto', 'va', 'la', 'gatta', 'al', 'lardo'], 3], 't!!t!d')
    counter_test_positivi += tester_fun(Ex5, [['tanto', 'va', 'la', 'gatta', 'al', 'lardo', 'che', 'ci', 'lascia', 'lo', 'zampino'], 4], 'o!!a!o!!i!i')
    counter_test_positivi += tester_fun(Ex5, [['nel', 'mezzo', 'del', 'cammin', 'di', 'nostra', 'vita', 'mi', 'ritrovai'], 6], '!!!!!!!!a')
    counter_test_positivi += tester_fun(Ex5, [['nel', 'mezzo', 'del', 'cammin', 'di', 'nostra', 'vita', 'mi', 'ritrovai'], 0], 'nmdcdnvmr')
    counter_test_positivi += tester_fun(Ex5, [[], 0],'')

    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

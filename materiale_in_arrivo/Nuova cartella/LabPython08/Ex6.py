def Ex6(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex6, [['jkl', 'h', 'plqa', 'a', 'xkj']] , {('jkl','xkj'), ('h','a'), ('a','h'), ('xkj','jkl')})
    counter_test_positivi += tester_fun(Ex6, [[]] , set())
    counter_test_positivi += tester_fun(Ex6, [['a', 'ab', 'abc']] , set())
    counter_test_positivi += tester_fun(Ex6, [['e', 'a', 'lp', 'ql', 'cl']] ,  {('e', 'a'), ('a', 'e'), ('lp', 'ql'), ('lp', 'cl'), ('ql', 'lp'), ('ql', 'cl'), ('cl', 'lp'), ('cl', 'ql')})
    counter_test_positivi += tester_fun(Ex6, [['hjkl', 'hjkp']] , {('hjkl', 'hjkp'), ('hjkp', 'hjkl')} )

    counter_test_positivi += tester_fun(Ex6, [['x', 'y']] , {('x', 'y'), ('y', 'x')} )
    counter_test_positivi += tester_fun(Ex6, [['Aa', 'Aa']] , set() )
    counter_test_positivi += tester_fun(Ex6, [['', '', 'A','B','C']] , {('A', 'B'), ('B', 'A'), ('A', 'C'), ('C', 'A'), ('B', 'C'), ('C', 'B')})
    counter_test_positivi += tester_fun(Ex6, [['A','AA','bcd']] , set())
    counter_test_positivi += tester_fun(Ex6, [['H','H']] , set())



    print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


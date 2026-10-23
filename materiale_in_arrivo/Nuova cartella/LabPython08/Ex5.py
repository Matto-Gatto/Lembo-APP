def Ex5(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex5, [['jkl', 'h', 'plqa', 'jkl', 'h', 'xkj']] , {('jkl',2), ('h',2), ('plqa',1), ('xkj',1)})
    counter_test_positivi += tester_fun(Ex5, [[]] , set())
    counter_test_positivi += tester_fun(Ex5, [['a', 'ab', 'abc']] , {('a', 1), ('ab', 1), ('abc', 1)})
    counter_test_positivi += tester_fun(Ex5, [['e', 'a', 'e', 'lp', 'a', 'ql', 'cl']] ,  {('e', 2), ('a', 2), ('lp', 1), ('ql', 1), ('cl', 1)} )
    counter_test_positivi += tester_fun(Ex5, [['hjkl', 'hjkl']] , {('hjkl', 2)})

    counter_test_positivi += tester_fun(Ex5, [['a', 'aa']] , {('a', 1), ('aa', 1)})
    counter_test_positivi += tester_fun(Ex5, [['a', 'a','a']] , {('a', 3)})
    counter_test_positivi += tester_fun(Ex5, [['','a','']] , {('a', 1), ('',2)})
    counter_test_positivi += tester_fun(Ex5, [['a','b','a','b','a']] , {('a', 3), ('b',2)})
    counter_test_positivi += tester_fun(Ex5, [['AAA','BBB','AAA']] , {('AAA', 2), ('BBB',1)})

    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


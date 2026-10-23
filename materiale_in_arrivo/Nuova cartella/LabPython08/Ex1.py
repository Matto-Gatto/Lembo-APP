def Ex1(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex1, [['casa', 'albero', 'bello']] , {'a','l'})
    counter_test_positivi += tester_fun(Ex1, [['ciao', 'ciao']] , set())
    counter_test_positivi += tester_fun(Ex1, [['aa','aa','hghjklhl']] , {'a','h','l'})
    counter_test_positivi += tester_fun(Ex1, [[]] , set())
    counter_test_positivi += tester_fun(Ex1, [['cogito', 'ergo', 'sum']] , {'o'})
    
    counter_test_positivi += tester_fun(Ex1, [['Aa', 'Aa', 'Aa']] , set())
    counter_test_positivi += tester_fun(Ex1, [['ZaZ', 'abca']] , {'Z','a'})
    counter_test_positivi += tester_fun(Ex1, [['1111111', '12345678']] , {'1'})
    counter_test_positivi += tester_fun(Ex1, [['abCdEfF', 'qwertya','g_g','zz','ZZ']] , {'g','z','Z'})
    counter_test_positivi += tester_fun(Ex1, [['a', 'a','aa']] , {'a'})


    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

def Ex8(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex8, [['amaca','amaranto','rosso']], {'a','o'})
    counter_test_positivi += tester_fun(Ex8, [['osso','assolato','alto']], {'o','a'})
    counter_test_positivi += tester_fun(Ex8, [['stringa','a','bbbbcccc','dado']], {'d','a','b'})
    counter_test_positivi += tester_fun(Ex8, [['fosso','dosso','rosso','fosso']], {'o'})
    counter_test_positivi += tester_fun(Ex8, [['ciao mamma','ciao ']], {' ','a'})

    counter_test_positivi += tester_fun(Ex8, [['tanto','va','la']], {'t','a'})
    counter_test_positivi += tester_fun(Ex8, [['assolato','alto']], {'a'})
    counter_test_positivi += tester_fun(Ex8, [['fondamenti','ssttzz','dado']], {'n','s','d'})
    counter_test_positivi += tester_fun(Ex8, [['armadio']], {'a'})
    counter_test_positivi += tester_fun(Ex8, [['morto','Dado']], {'o','D'})

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

def Ex2(l1,l2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""        

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, [['arco', 'pippo', 'pluto', 'corda'],['palla', 'darco', 'ocra', 'casa']],{'corda', 'darco', 'ocra', 'arco'})
    counter_test_positivi += tester_fun(Ex2, [['arco', 'pala', 'pluto', 'corda'],['palla', 'caro', 'ocra', 'casa']],{'caro', 'arco', 'ocra'})
    counter_test_positivi += tester_fun(Ex2, [['arco', 'pala', '', 'corda'],['palla', 'codarco', 'ocra', 'casa', '']],{'', 'arco', 'ocra'})
    counter_test_positivi += tester_fun(Ex2, [['arco', 'pippo', 'pluto', 'corda'],[]],set())
    counter_test_positivi += tester_fun(Ex2, [['arco', 'caro','pluto'],['tuplo', 'acaro']],{'pluto', 'tuplo'})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

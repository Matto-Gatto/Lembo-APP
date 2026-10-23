def Ex8(s):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun
    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex8, ['caso palese'] ,'ase')
    counter_test_positivi += tester_fun(Ex8, ['caso palesemente'] ,'e')
    counter_test_positivi += tester_fun(Ex8, ['caso palese zitto'] ,'aso et')
    counter_test_positivi += tester_fun(Ex8, ['aca'] ,'a')
    counter_test_positivi += tester_fun(Ex8, [''] ,'')

    counter_test_positivi += tester_fun(Ex8, ['aaabbbccc'] ,'abc')
    counter_test_positivi += tester_fun(Ex8, ['aabaaaccefcccc'] ,'c')
    counter_test_positivi += tester_fun(Ex8, ['abcabcabcabcabcdddd'] ,'abc')
    counter_test_positivi += tester_fun(Ex8, ['a'] ,'a')
    counter_test_positivi += tester_fun(Ex8, ['ccccababab'] ,'c')

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

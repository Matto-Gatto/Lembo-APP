def Ex11(b1,b2):
   """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun
    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex11, ['1011','100'],'1000')
    counter_test_positivi += tester_fun(Ex11, ['','111'],'000')
    counter_test_positivi += tester_fun(Ex11, ['1','1'],'1')
    counter_test_positivi += tester_fun(Ex11, ['111','10'],'100')
    counter_test_positivi += tester_fun(Ex11, ['1010',''],'0000')

    counter_test_positivi += tester_fun(Ex11, ['0011','101'],'0010')
    counter_test_positivi += tester_fun(Ex11, ['','10111'],'00000')
    counter_test_positivi += tester_fun(Ex11, ['0','1'],'0')
    counter_test_positivi += tester_fun(Ex11, ['010','11'],'010')
    counter_test_positivi += tester_fun(Ex11, ['010101',''],'000000')

    print('La funzione',Ex11.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

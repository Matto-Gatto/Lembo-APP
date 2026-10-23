def Ex5(s):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun
    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex5, ['223367'],True)
    counter_test_positivi += tester_fun(Ex5, ['1234567890'],False)
    counter_test_positivi += tester_fun(Ex5, ['2211003367'],False)
    counter_test_positivi += tester_fun(Ex5, ['1234567899'],True)
    counter_test_positivi += tester_fun(Ex5, ['2234567'],False)

    counter_test_positivi += tester_fun(Ex5, [''],False)
    counter_test_positivi += tester_fun(Ex5, ['12345'],False)
    counter_test_positivi += tester_fun(Ex5, ['0'],True)
    counter_test_positivi += tester_fun(Ex5, ['9999999999'],True)
    counter_test_positivi += tester_fun(Ex5, ['0123456788'],True)

    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

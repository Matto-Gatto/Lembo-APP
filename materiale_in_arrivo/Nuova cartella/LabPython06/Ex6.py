def Ex6(s,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun
    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex6, ['stringa di prova',3],'rio')
    counter_test_positivi += tester_fun(Ex6, ['stringa di prova',2],'trn dpv')
    counter_test_positivi += tester_fun(Ex6, ['stringa di prova',5],'sind')
    counter_test_positivi += tester_fun(Ex6, ['',1],'')
    counter_test_positivi += tester_fun(Ex6, ['stringa di prova stringa di prova',4],'t dp')

    counter_test_positivi += tester_fun(Ex6, ['abcabc',1],'abc')
    counter_test_positivi += tester_fun(Ex6, ['abcccaa',100],'')
    counter_test_positivi += tester_fun(Ex6, ['un insieme di lettere',5],'nisd')
    counter_test_positivi += tester_fun(Ex6, ['un insieme di lettere',2],'n dltr')
    counter_test_positivi += tester_fun(Ex6, ['',3],'')


    print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


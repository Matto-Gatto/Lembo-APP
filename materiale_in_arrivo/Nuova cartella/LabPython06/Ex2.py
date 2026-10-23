def Ex2(s,c):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, ['AzzuRRO','a'],'zzu')
    counter_test_positivi += tester_fun(Ex2, ['AzzuRRO','A'],'zzuRRO')
    counter_test_positivi += tester_fun(Ex2, ['Albergo','b'],'lergo')
    counter_test_positivi += tester_fun(Ex2, ['Roma','E'],'Roma')
    counter_test_positivi += tester_fun(Ex2, ['barca','s'],'')

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


def Ex1(l):
    """ INSERISCI QUI LA TUA SOLUZIONE """
            


    """INSERITE QUI LA VOSTRA SOLUZIONE"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, [['blink182','sole','circo','alfa0','B20']] ,['alfa0','circo','sole'])
    counter_test_positivi += tester_fun(Ex1, [['non','ci','sono','parole','da','eliminare']] ,['ci','da','eliminare','non','parole','sono'])
    counter_test_positivi += tester_fun(Ex1, [['codice11','MI-34','asso','A11']] ,['asso'])
    counter_test_positivi += tester_fun(Ex1, [['34','24ore','linea12']] ,[])
    counter_test_positivi += tester_fun(Ex1, [['i5','','W23X','ciao']] ,['','ciao','i5'])
    
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
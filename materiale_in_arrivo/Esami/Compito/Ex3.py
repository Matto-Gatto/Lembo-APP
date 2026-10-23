def Ex3(file):
    """ INSERISCI QUI LA TUA SOLUZIONE """

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5


    counter_test_positivi += tester_fun(Ex3, ['file1.csv'],{'Alberto','Maria'})
    counter_test_positivi += tester_fun(Ex3, ['file2.csv'],{'Alberto','Marco'})
    counter_test_positivi += tester_fun(Ex3, ['file3.csv'],{'Giovanni'})
    counter_test_positivi += tester_fun(Ex3, ['file4.csv'],set())
    counter_test_positivi += tester_fun(Ex3, ['file5.csv'],{'Maria'})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
            
    


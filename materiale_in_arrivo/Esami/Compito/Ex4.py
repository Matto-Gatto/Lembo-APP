def Ex4(l):
    """ INSERISCI QUI LA TUA SOLUZIONE """

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5


    counter_test_positivi += tester_fun(Ex4, [[('Mario',27),('Fabio',28),('Mario',30),('Luca',18),('Luca',21)]],{'Mario':30,'Fabio':28,'Luca':21})
    counter_test_positivi += tester_fun(Ex4, [[('Marco',24),('Marco',28),('Marco',27),('Marco',29)]],{'Marco':29})
    counter_test_positivi += tester_fun(Ex4, [[('Maria',27),('Alberta',28)]],{'Maria':27,'Alberta':28})
    counter_test_positivi += tester_fun(Ex4, [[('Riccardo',25),('Fabio',25),('Riccardo',30)]],{'Riccardo':30,'Fabio':25})
    counter_test_positivi += tester_fun(Ex4, [[('Sonia',26),('Michele',28),('Michele',30),('Sonia',28),('Sonia',30)]],{'Sonia':30,'Michele':30})

print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

            
    


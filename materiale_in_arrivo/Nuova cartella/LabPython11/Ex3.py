def Ex3(file1,file2):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['menu1.csv','ordini1.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66})
    counter_test_positivi += tester_fun(Ex3, ['menu1.csv','ordini2.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66, 'Daniele': 36})
    counter_test_positivi += tester_fun(Ex3, ['menu2.csv','ordini3.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66, 'Daniele': 36, 'Fabio': 'respinto'})
    counter_test_positivi += tester_fun(Ex3, ['menu3.csv','ordini4.csv'],{'Giorgio': 'respinto', 'Paola': 'respinto', 'Francesca': 'respinto', 'Filippo': 'respinto'}) # tutti respinti
    counter_test_positivi += tester_fun(Ex3, ['menu4.csv','ordini5.csv'],{'Giorgio': 'respinto', 'Paola': 72, 'Francesca': 66})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

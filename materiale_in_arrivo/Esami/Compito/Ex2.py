def Ex2(file):
    """ INSERISCI QUI LA TUA SOLUZIONE """

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt'],{5: 'tanto', 2: 'va', 3: 'chi', 6: 'lascia', 7: 'zampino', 1: 'a', 4: 'roma', 8: 'poltrona'})    
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt'],{5: 'legge', 2: 'le', 7: 'trovato', 9: 'schiaccia', 6: 'chiodo'})   
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt'],{5: 'volli', 1: 'e', 6: 'sempre', 15: 'fortissimamente', 2: 'la'})   
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt'],{2: 'sa', 7: 'pentole', 3: 'più', 1: 'i', 8: 'coperchi', 5: 'tanto', 6: 'onesta', 4: 'pare'}) 
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt'],{3: 'tre', 5: 'tigri', 6: 'uccidi', 12: 'moschettieri', 2: 'se'})
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

    

def Ex3(file,nome):           
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
	
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, ["puntiPartite_1.txt","Luka"], 53)
    counter_test_positivi += tester_fun(Ex3, ["puntiPartite_1.txt","Jimmy"], 38)
    counter_test_positivi += tester_fun(Ex3, ["puntiPartite_1.txt","Larry"], 0)
    counter_test_positivi += tester_fun(Ex3, ["puntiPartite_2.txt","Bianchi"] , 76)
    counter_test_positivi += tester_fun(Ex3, ["puntiPartite_2.txt","Rossi"] , 64)

    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

def Ex9(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
            
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex9, [["casa", "senape", "ketchup", "pasta"]] , "s")
    counter_test_positivi += tester_fun(Ex9, [["a", "b", "b", "a", "a", "a", "a"]] , "a")
    counter_test_positivi += tester_fun(Ex9, [["1fI", "1FI", "1FI", "1FI","1FI" ]] , "f")
    counter_test_positivi += tester_fun(Ex9, [["conte", "dpcm"]] , "c")
    counter_test_positivi += tester_fun(Ex9, [["Zlatan", "Ibraimovich", "Cristiano", "Ronaldo", "Francesco", "Totti"]] , "o")
    
    counter_test_positivi += tester_fun(Ex9, [["z", "a", "a", "z"]] , "z")
    counter_test_positivi += tester_fun(Ex9, [["A", "A", "A", "b"]] , "b")
    counter_test_positivi += tester_fun(Ex9, [["a", "a", "a", "b"]] , "a")
    counter_test_positivi += tester_fun(Ex9, [["1", "123", "11_a_22", "123c456","wwaww"]] , "a")
    counter_test_positivi += tester_fun(Ex9, [["Zb"]] , "b")

    print('La funzione',Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


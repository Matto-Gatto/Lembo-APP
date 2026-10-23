from tester import tester_fun

def A_Ex3(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ['vendite1.csv'] ,['Mario'])
counter_test_positivi += tester_fun(A_Ex3, ['vendite2.csv'] ,['Gianni', 'Mario', 'Paolo'])
counter_test_positivi += tester_fun(A_Ex3, ['vendite3.csv'] ,['Gianni', 'Paolo'])
counter_test_positivi += tester_fun(A_Ex3, ['vendite4.csv'] ,['Gianni', 'Maria', 'Paolo'] )
counter_test_positivi += tester_fun(A_Ex3, ['vendite5.csv'] ,['Paolo'] )

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

from tester import tester_fun

def D_Ex3(file,ore,minuti):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(D_Ex3, ['ritardi1.csv',12,20] ,['54200','6310'])
counter_test_positivi += tester_fun(D_Ex3, ['ritardi2.csv',12,20] ,['54200', '6310', '79001'])
counter_test_positivi += tester_fun(D_Ex3, ['ritardi1.csv',10,20] ,[])
counter_test_positivi += tester_fun(D_Ex3, ['ritardi2.csv',11,40] ,['54200'] )
counter_test_positivi += tester_fun(D_Ex3, ['ritardi3.csv',14,20] ,['54200', '6310', '6550', '79001'])

print('La funzione',D_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

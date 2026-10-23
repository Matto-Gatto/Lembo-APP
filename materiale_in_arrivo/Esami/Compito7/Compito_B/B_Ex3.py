from tester import tester_fun

def B_Ex3(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, ['file1.csv'],{'Lavatrice':3,'Televisore':1})
counter_test_positivi += tester_fun(B_Ex3, ['file2.csv'],{'Frigorifero':3,'PS4':3})
counter_test_positivi += tester_fun(B_Ex3, ['file3.csv'],{})
counter_test_positivi += tester_fun(B_Ex3, ['file4.csv'],{'Televisore':3,'Frigorifero':1})
counter_test_positivi += tester_fun(B_Ex3, ['file5.csv'],{'Decoder':50,'Frigorifero':1,'Forno':1})

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

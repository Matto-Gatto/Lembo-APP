from tester import tester_fun

def B_Ex2(file,diz):
 """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, ['file1.txt',{'Francia':'0033','Italia':'0039'}] ,{'0033056784435'})
counter_test_positivi += tester_fun(B_Ex2, ['file2.txt',{'Spagna':'0034','Italia':'0039','UK':'0044'}],{'004411234', '003933445567'})
counter_test_positivi += tester_fun(B_Ex2, ['file3.txt',{'Spagna':'0034','Italia':'0039'}] ,{'003933445567', '0034772749270'})
counter_test_positivi += tester_fun(B_Ex2, ['file4.txt',{'Germania':'0049','Italia':'0039'}] ,{'003933445566', '0049223345'})
counter_test_positivi += tester_fun(B_Ex2, ['file5.txt',{'Germania':'0049','UK':'0044'}] ,set())

print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


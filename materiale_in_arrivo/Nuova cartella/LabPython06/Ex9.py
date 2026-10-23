def Ex9(s1,s2):
   """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
   from tester import tester_fun
   """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

   counter_test_positivi = 0
   total_tests = 10

   counter_test_positivi += tester_fun(Ex9, ['caso palese','casa blue'],4)
   counter_test_positivi += tester_fun(Ex9, ['caso palese','casata blue'],3)
   counter_test_positivi += tester_fun(Ex9, ['caso palese','casacca blue sole'],3)
   counter_test_positivi += tester_fun(Ex9, ['','casa blue'],0)
   counter_test_positivi += tester_fun(Ex9, ['',''],0)

   counter_test_positivi += tester_fun(Ex9, ['abc',''], 0)
   counter_test_positivi += tester_fun(Ex9, ['abcde','abcdep'], 5)
   counter_test_positivi += tester_fun(Ex9, ['abcde','eb acdp'], 5)
   counter_test_positivi += tester_fun(Ex9, ['abcde','fghi'], 0)
   counter_test_positivi += tester_fun(Ex9, ['abcabcabcw','bbccbcww'], 2)

   print('La funzione',Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

from tester import tester_fun

def A_Ex2(file):
      d = {}
      f = open(file,encoding = 'UTF-8')
      for riga in f:
            parole = riga.strip().split()
            for i in range(len(parole)):
                  parola = parole[i]
                  if parole[i:].count(parola) == 1:
                        d[parola] = d.get(parola,0) + 1
      parola = ''
      for elem in d:
            if d[elem] >= 3 and (len(elem) > len(parola) or (len(elem) == len(parola) and elem < parola)):
                  parola = elem
      return parola
       
                          
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, ['file1.txt'],'albero')
counter_test_positivi += tester_fun(A_Ex2, ['file2.txt'],'giovane')
counter_test_positivi += tester_fun(A_Ex2, ['file3.txt'],'casolare')
counter_test_positivi += tester_fun(A_Ex2, ['file4.txt'],'giovane')
counter_test_positivi += tester_fun(A_Ex2, ['file5.txt'],'')

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

from tester import tester_fun

def Ex3(file):
    f=open(file,'r',encoding='UTF-8')
    d={} # uso un dizionario per tenere traccia delle occorrenze dei numeri
    l=[] # lista da restituire, inizialmente vuota
    for riga in f:
        riga=riga.strip().split(',')
        for elem in riga:
            if elem not in d:
                d[elem]=1
            else:
                d[elem]=d[elem]+1
    if d!={}:
        valori=d.values()
        massimo=max(valori)
    for k in d:
        if d[k]==massimo:
            l.append(int(k))
    l.sort()
    return l

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 10

counter_test_positivi += tester_fun(Ex3, ['ruota1.csv'],[14,50])
counter_test_positivi += tester_fun(Ex3, ['ruota2.csv'],[2,14])
counter_test_positivi += tester_fun(Ex3, ['ruota3.csv'],[2])
counter_test_positivi += tester_fun(Ex3, ['ruota4.csv'],[24,43,47,50])
counter_test_positivi += tester_fun(Ex3, ['ruota5.csv'],[])

counter_test_positivi += tester_fun(Ex3, ['ruota6.csv'],[56,75])
counter_test_positivi += tester_fun(Ex3, ['ruota7.csv'],[2,12,14])
counter_test_positivi += tester_fun(Ex3, ['ruota8.csv'],[3])
counter_test_positivi += tester_fun(Ex3, ['ruota9.csv'],[2,15,43])
counter_test_positivi += tester_fun(Ex3, ['ruota10.csv'],[4,33,55,60,81])

print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

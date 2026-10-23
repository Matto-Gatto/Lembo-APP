from tester import tester_fun

def B_Ex3(file):
    f = open(file,'r',encoding='UTF-8')
    d = {}
    for riga in f:
        lista = riga.strip().split(',')
        treno = lista[0]
        stazione = lista[1]
        ap = lista[2]
        if stazione not in d:
            d[stazione] = []
        if ap == 'A':
            if treno in d[stazione]:
                d[stazione].remove(treno)
        else:
            if treno not in d[stazione]:
                d[stazione].append(treno)
                d[stazione].sort()
    return d
            
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, ['treni1.csv'],{'Termini': ['T72', 'T81'], 'Tiburtina': ['T61'], 'Trastevere': []})
counter_test_positivi += tester_fun(B_Ex3, ['treni2.csv'],{'Termini': ['T72', 'T81'], 'Tiburtina': ['T61'], 'Trastevere': ['T53']})
counter_test_positivi += tester_fun(B_Ex3, ['treni3.csv'],{'Termini': ['T72'], 'Tiburtina': ['T61'], 'Trastevere': ['T53', 'T81']})
counter_test_positivi += tester_fun(B_Ex3, ['treni4.csv'],{'Termini': ['T72'], 'Tiburtina': ['T53', 'T61'], 'Trastevere': ['T81']})
counter_test_positivi += tester_fun(B_Ex3, ['treni5.csv'],{'Termini': ['T12', 'T72'], 'Tiburtina': ['T53', 'T61'], 'Trastevere': ['T81'], 'SanPietro': []})

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

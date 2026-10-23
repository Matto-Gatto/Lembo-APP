from tester import tester_fun

def B_Ex2(l):
    massimo=0
    lista=[]
    for e in l:
        cont=0
        for c in e:
            if c.islower():
                cont+=1
        if cont>massimo:
            massimo=cont
            lista=[e]
        elif cont==massimo:
            lista.append(e)
    i=0
    while i < len(l):
        if l[i] in lista:
            l=l[:i+1]+[l[i]]+l[i+1:]
            i=i+2
        else:
            i=i+1        
    return l

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, [["piPPo", "PIppO", "PLuto", "PiPPo"]] ,["piPPo", "piPPo", "PIppO","PLuto", "PLuto", "PiPPo"])
counter_test_positivi += tester_fun(B_Ex2, [["mamma", "pippo", "Pluto", "Pluto"]]  ,["mamma", "mamma", "pippo", "pippo", "Pluto", "Pluto"])
counter_test_positivi += tester_fun(B_Ex2, [["ACME", "ACM"]] ,["ACME","ACME", "ACM","ACM"])
counter_test_positivi += tester_fun(B_Ex2, [[""]] ,["",""])
counter_test_positivi += tester_fun(B_Ex2, [["ciao","ciao"]] ,["ciao","ciao","ciao","ciao"])

print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


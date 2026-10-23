from tester import tester_fun

def A_Ex2(l):
    massimo=0
    lista=[]
    for e in l:
        cont=0
        for c in e:
            if c.isupper():
                cont+=1
        if cont>massimo:
            massimo=cont
            lista=[e]
        elif cont==massimo:
            lista.append(e)
    i=0
    while i<len(l):
        if l[i] in lista:
            l.remove(l[i])
        else:
            i = i+1
    return l


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [["piPPo", "pippo","PLuto","Pippo"]],["pippo","Pippo"])
counter_test_positivi += tester_fun(A_Ex2, [["Maria", "mamma","Monica"]] ,["mamma"])
counter_test_positivi += tester_fun(A_Ex2, [["","questa è una stringa"]] ,[])
counter_test_positivi += tester_fun(A_Ex2, [["Ciao","ciao"]] ,["ciao"])
counter_test_positivi += tester_fun(A_Ex2, [["gennaio","FEbbraio","Marzo"]] ,["gennaio","Marzo"])

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

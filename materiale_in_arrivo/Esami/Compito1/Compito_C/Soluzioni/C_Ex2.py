from tester import tester_fun

def C_Ex2(l1,l2):
    ris=[]
    for i in range(len(l1)):
        cont=0
        for j in range(len(l1[i])):
            if l1[i][j] in l2[i] and l1[i][j] not in l1[i][:j]:
                cont+=1        
        ris.append(l1[i])
        ris.append(cont)
    return ris

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex2, [["mamma", "asso", "re", "pluto"],["mare", "lago", "fante", "barba"]] ,["mamma", 2, "asso", 2, "re", 1, "pluto", 0])
counter_test_positivi += tester_fun(C_Ex2, [["","aaa"],["regina","fante"]] ,["",0,"aaa",1])
counter_test_positivi += tester_fun(C_Ex2, [["re","regina","cavallo"],["re","cavallo","regina"]] ,["re",2,"regina",1,"cavallo",1])
counter_test_positivi += tester_fun(C_Ex2, [["","aaa"],["","aaa"]] ,["",0,"aaa",1])
counter_test_positivi += tester_fun(C_Ex2, [["Marea"],["marea"]],["Marea",3])

print('La funzione',C_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


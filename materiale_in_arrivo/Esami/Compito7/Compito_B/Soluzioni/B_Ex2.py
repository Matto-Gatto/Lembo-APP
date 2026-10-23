from tester import tester_fun

def B_Ex2(file,diz):
    f=open(file,'r',encoding='UTF-8')
    testo=f.read()
    ris=set()
    lista = testo.split()
    for i in range(len(lista)-1):
        if lista[i].isdigit() and 5 <= len(lista[i]) <= 9 and lista[i+1][0]=='(' and lista[i+1][-1]==')':
            nazione=lista[i+1][1:len(lista[i+1])-1]
            if nazione in diz:
                ris.add(diz[nazione]+lista[i])
    return ris

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 10

counter_test_positivi += tester_fun(B_Ex2, ['file1.txt',{'Francia':'0033','Italia':'0039'}] ,{'0033056784435'})
counter_test_positivi += tester_fun(B_Ex2, ['file2.txt',{'Spagna':'0034','Italia':'0039','UK':'0044'}],{'004411234', '003933445567'})
counter_test_positivi += tester_fun(B_Ex2, ['file3.txt',{'Spagna':'0034','Italia':'0039'}] ,{'003933445567', '0034772749270'})
counter_test_positivi += tester_fun(B_Ex2, ['file4.txt',{'Germania':'0049','Italia':'0039'}] ,{'003933445566', '0049223345'})
counter_test_positivi += tester_fun(B_Ex2, ['file5.txt',{'Germania':'0049','UK':'0044'}] ,set())

counter_test_positivi += tester_fun(B_Ex2, ['file6.txt',{'Francia':'0033', 'Portogallo':'00351', 'Italia':'0039'}] ,{'0033911667','003517734567'})
counter_test_positivi += tester_fun(B_Ex2, ['file7.txt',{'Brasile':'0055', 'UK':'0044', 'Germania':'0049'}] ,{'005533445567','004411235'})
counter_test_positivi += tester_fun(B_Ex2, ['file8.txt',{'Brasile':'0055', 'UK':'0044', 'Germania':'0049'}] ,{'005533445567','004977274927','004411235'})
counter_test_positivi += tester_fun(B_Ex2, ['file9.txt',{'Brasile':'0055'}] ,{'005533445567'})
counter_test_positivi += tester_fun(B_Ex2, ['file10.txt',{'Italia':'0039','Spagna':'0034'}] ,{'003912345','003412345'})

print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


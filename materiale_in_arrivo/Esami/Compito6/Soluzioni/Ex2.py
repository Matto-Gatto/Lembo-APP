from tester import tester_fun

def Ex2(file):
    f=open(file,'r',encoding='UTF-8')
    testo=f.read()
    d={}
    lista=testo.split()
    for m in lista:
        if m.count('@')==1:
            email=m
            j=email.rfind('.') # j è la posizione dell'ultimo punto
            h=email.rfind('@') # h è la posizione della chiocciola
            k=email.rfind('.',0,j) # k è la posizione del penultimo punto
            if h > k:
                k=h # il dominio si trova fra @ ed il .
            dominio=email[k+1:j]
            d[dominio]=d.get(dominio,set())|{email[0:h]}
    return d

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 10

counter_test_positivi += tester_fun(Ex2, ['file1.txt'] ,{'gmail':{'marco.marco'},'uniroma1':{'anna'}})
counter_test_positivi += tester_fun(Ex2, ['file2.txt'] ,{'gmail':{'alberto','marco.marco'},'tiscali':{'anna'},'uniroma1':{'alberto'}})
counter_test_positivi += tester_fun(Ex2, ['file3.txt'] ,{'gmail':{'marco.rossi'},'yahoo':{'rossi'},'apple':{'giorgio.bianchi','marco.rossi','rossi'},'microsoft':{'bianchi'},'ping':{'ferro','paolo.ferro'}})
counter_test_positivi += tester_fun(Ex2, ['file4.txt'] ,{'uniroma1':{'marco.rossi','giorgio.bianchi'},'yahoo':{'rossi'},'tuwien':{'bianchi'}})
counter_test_positivi += tester_fun(Ex2, ['file5.txt'] ,{'uniroma1':{'marco.rossi','neri','verdi'}})

counter_test_positivi += tester_fun(Ex2, ['file6.txt'] ,{'gmail':{'gio.gio'},'uniroma2':{'marta'}})
counter_test_positivi += tester_fun(Ex2, ['file7.txt'] ,{'bing':{'aldo.aldo','alberto'},'miodominio':{'piero'},'uniroma1':{'alberto'}})
counter_test_positivi += tester_fun(Ex2, ['file8.txt'] ,{'yahoo':{'verdi','bianchi'},'bing':{'piombo','paolo.piombo','giorgio.verdi'},'apple':{'sara.bianchi'}})
counter_test_positivi += tester_fun(Ex2, ['file9.txt'] ,{'uniroma2':{'marco.rossi','giorgio.bianchi'},'yes':{'rossi'},'tuwien':{'bianchi'}})
counter_test_positivi += tester_fun(Ex2, ['file10.txt'] ,{'uniroma3':{'gallo','neri'}})

print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


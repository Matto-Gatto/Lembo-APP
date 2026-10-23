from tester import tester_fun

def B_Ex3(file):
    f=open(file,'r',encoding='UTF-8')
    d={} # uso un dizionario per tenere traccia del numero di unità per ciascun prodotto in magazzino dei numeri
    ris={} # dizionario da restituire, inizialmente vuoto
    f.readline()
    for riga in f:
        riga=riga.strip().split(',')
        prodotto=riga[0]
        quantita=int(riga[1])
        if quantita>=0: # si deposita in magazzino
            d[prodotto]=d.get(prodotto,0)+quantita
        else: # si effettua un prelievo dal magazzino
            if d.get(prodotto,0) >= abs(quantita):
                d[prodotto]=d.get(prodotto,0)+quantita
            else:
                ris[prodotto]=ris.get(prodotto,0)+abs(d.get(prodotto,0)+quantita)
                d[prodotto]=0
    return ris

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 10

counter_test_positivi += tester_fun(B_Ex3, ['file1.csv'],{'Lavatrice':3,'Televisore':1})
counter_test_positivi += tester_fun(B_Ex3, ['file2.csv'],{'Frigorifero':3,'PS4':3})
counter_test_positivi += tester_fun(B_Ex3, ['file3.csv'],{})
counter_test_positivi += tester_fun(B_Ex3, ['file4.csv'],{'Televisore':3,'Frigorifero':1})
counter_test_positivi += tester_fun(B_Ex3, ['file5.csv'],{'Decoder':50,'Frigorifero':1,'Forno':1})

counter_test_positivi += tester_fun(B_Ex3, ['file6.csv'],{'Sci':3,'Racchetta':1})
counter_test_positivi += tester_fun(B_Ex3, ['file7.csv'],{'Pallone':6})
counter_test_positivi += tester_fun(B_Ex3, ['file8.csv'],{'Frigorifero':1})
counter_test_positivi += tester_fun(B_Ex3, ['file9.csv'],{'Stereo':3,'Modem':1})
counter_test_positivi += tester_fun(B_Ex3, ['file10.csv'],{'Penna':50,'Forno':1})

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

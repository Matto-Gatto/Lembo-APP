def Ex6(file):
    ## si consiglia di aiutarsi usando i seguente dizionario che riporta per ogni mese
    ## una lista il cui primo elemento è la stringa da usare per identificare
    ## il mese in una data nel formato gg/mm/aaa, ed il cui secondo elemento è
    ## il numero di giorni del mese.
    mesi = {'A': ['01',31],'B' : ['02',28],'C': ['03',31],'D' :['04',30],
            'E': ['05',30],'H': ['06',30],'L':['07',31],'M': ['08',31],
            'P': ['09',30],'R': ['10',31],'S': ['11',30],'T':['12',31]}    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""   
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex6, ["codici1.txt"] , ['12/03/1971', '18/11/1921', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex6, ["codici2.txt"] , ['12/03/1971', '18/11/1921', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', '30/11/1981', '07/03/1991'])
    counter_test_positivi += tester_fun(Ex6, ["codici3.txt"] , ['30/03/1971', '01/11/2017','01/11/1921'])
    counter_test_positivi += tester_fun(Ex6, ["codici4.txt"] , ['21/08/1972','15/04/2007', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex6, ["codici5.txt"] , ['01/11/1931', 'Mese errato', 'Giorno errato'])

    print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

def Ex2(l,c,n):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    """SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA CON #"""
    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex2, [['palla','casse','palo'],'a',2] ,['casse','palo'])
    counter_test_positivi += tester_fun(Ex2, [['palla','casse','palo'],'p',1] ,['casse'])
    counter_test_positivi += tester_fun(Ex2, [['pallone','casse','palla','pappa'],'p',2] ,['pallone','casse','palla'])
    counter_test_positivi += tester_fun(Ex2, [['pallone','casse','palla','pappa'],'a',1], [])
    counter_test_positivi += tester_fun(Ex2, [[],'a',1] , [])

    counter_test_positivi += tester_fun(Ex2, [['aa','aa','aa'],'a',2] ,[])
    counter_test_positivi += tester_fun(Ex2, [['aa','aa','aa'],'a',3] ,['aa','aa','aa'])
    counter_test_positivi += tester_fun(Ex2, [['aa','aa','aa'],'z',1] ,['aa','aa','aa'])
    counter_test_positivi += tester_fun(Ex2, [['z','aa','zz','aa','aa'],'z',1] ,['aa','aa','aa'])
    counter_test_positivi += tester_fun(Ex2, [['a','aa','aaa'],'a',3] ,['a','aa'])

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

from tester import tester_fun

def Ex1(s):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
            
###############################################################################

"""NON MODIFICARE -- codice di testing della funzione"""

"""Se non volete svolgere un test, commentate la riga corrispondente"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, ['tanto gatta  lardo lascia orto ala'],'orto')
    counter_test_positivi += tester_fun(Ex1, ['tanto gatta  lardo lascia arto ala'],'ala')
    counter_test_positivi += tester_fun(Ex1, ['asta enorme'],'enorme')
    counter_test_positivi += tester_fun(Ex1, ['palla perpep asta'],'perpep')
    counter_test_positivi += tester_fun(Ex1, ['a aa bb'],'aa')


    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

                

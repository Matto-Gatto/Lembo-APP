from Persona import *

def Ex5(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex5, ['persone1.csv'],[Persona('Aurora',1988),Persona('Elena',1998),Persona('Mario',1972),Persona('Sara',2003)])
    counter_test_positivi += tester_fun(Ex5, ['persone2.csv'],[Persona('Alberto',1972),Persona('Barbara',1988),Persona('Carlo',2003)])
    counter_test_positivi += tester_fun(Ex5, ['persone3.csv'],[Persona('Marco',1980),Persona('Sandro',1970)])
    counter_test_positivi += tester_fun(Ex5, ['persone4.csv'],[])
    counter_test_positivi += tester_fun(Ex5, ['persone5.csv'],[Persona('Maria',2000),Persona('Michela',2000),Persona('Michele',2000)])
    

    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

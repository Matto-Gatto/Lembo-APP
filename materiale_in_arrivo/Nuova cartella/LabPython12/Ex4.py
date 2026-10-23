from Persona import *

def Ex4(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex4, [[Persona('mario',1952),Persona('anna',1952),Persona('aldo',1970)]],{1952:{'mario','anna'},1970:{'aldo'}})
    counter_test_positivi += tester_fun(Ex4, [[Persona('mario',1952),Persona('anna',1952),Persona('aldo',1970),Persona('john',1970),Persona('mike',1970)]],{1952:{'mario','anna'},1970:{'aldo','mike','john'}})
    counter_test_positivi += tester_fun(Ex4, [[Persona('stefano',2001),Persona('marta',2001)]],{2001:{'stefano','marta'}})
    counter_test_positivi += tester_fun(Ex4, [[Persona('frank',2000)]],{2000:{'frank'}})
    counter_test_positivi += tester_fun(Ex4, [[]],{})

    print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

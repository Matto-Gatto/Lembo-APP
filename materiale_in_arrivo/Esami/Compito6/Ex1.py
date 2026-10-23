from tester import tester_fun

def Ex1(s1,s2):
    """Inserite qui la vostra soluzione"""

###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex1, ['allegria', 'jeah'], 'eaallgri')
counter_test_positivi += tester_fun(Ex1, ['allegria', ''], 'allegria')
counter_test_positivi += tester_fun(Ex1, ['dghhlf', 'hdgle'], 'hhdglf')
counter_test_positivi += tester_fun(Ex1, ['ba', 'ab'], 'ab')
counter_test_positivi += tester_fun(Ex1, ['entertainment', 'ae'], 'aeeentrtinmnt')

print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

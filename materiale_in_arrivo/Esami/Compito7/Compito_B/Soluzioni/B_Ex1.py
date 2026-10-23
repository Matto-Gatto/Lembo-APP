from tester import tester_fun

def B_Ex1(s):
    r=''
    i=0
    while(i<len(s)):
        c=s[i]
        j=i
        n=0
        finito=False
        while(j<len(s) and not finito):
            if (s[i]==s[j]):
                n=n+1
                j=j+1
            else:
                finito=True
        i=j
        r=r+str(n)+c
    return r


###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 10

counter_test_positivi += tester_fun(B_Ex1, ["WWWWEERWWRRRFF"] , "4W2E1R2W3R2F")
counter_test_positivi += tester_fun(B_Ex1, ["sTTTFFL"] , "1s3T2F1L")
counter_test_positivi += tester_fun(B_Ex1, [""] , "")
counter_test_positivi += tester_fun(B_Ex1, ["a"] , "1a")
counter_test_positivi += tester_fun(B_Ex1, ["aaaahhajjllhhhh"] , "4a2h1a2j2l4h")

counter_test_positivi += tester_fun(B_Ex1, ["abababccc"] , "1a1b1a1b1a1b3c")
counter_test_positivi += tester_fun(B_Ex1, ["wwwkkjjaaaaa"] , "3w2k2j5a")
counter_test_positivi += tester_fun(B_Ex1, [""] , "")
counter_test_positivi += tester_fun(B_Ex1, ["cccac"] , "3c1a1c")
counter_test_positivi += tester_fun(B_Ex1, ["sadppppdddl"] , "1s1a1d4p3d1l")

print('La funzione',B_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

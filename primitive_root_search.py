import sys
import math
from math import sqrt

def fpa_2(x,e,m):
    y=int(1)
    while e!=0:
        if e%2==0:
            x=int((x*x)%m)
            e=int(e/2)
        else:
            e=int(e-1)
            y=int((x*y)%m)
    return y


def findPrimefactors(s, n) :
    while (n % 2 == 0) :
        s.append(2)
        n = n // 2
    for i in range(3, int(sqrt(n)), 2):
        while (n % i == 0) :
 
            s.append(i)
            n = n // i
    if (n > 2) :
        s.append(n)

def primitive_root_search(p):
    q=[]
    
    findPrimefactors(q,p-1)

    root_set=[]
    for b in range(2,p):
        flag=True
        for divisor in q:
            if 1 == fpa_2(b,(p-1)/divisor,p):
                flag=False
                break
        if flag:
            print(f'{b} is primitive root of {p}')
            root_set.append(b)
            break
    return root_set
        
p=int(sys.argv[1])

root=primitive_root_search(p)
for x in root:
    for e in range(0,p):
        if fpa_2(x,e,p) == 1 and e!=0:
            print(f'{x}^{e} mod {p} = 1')
            break
    

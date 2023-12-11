import sys
import math

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def fpa_2(x,e,m):
    y=int(1)
    while e!=0:
        if e%2==0:
            x=int((x*x)%m)
            e=int(e/2)
        else:
            e=int(e-1)
            y=int((x*y)%m)
        print(f'{x}\t{e}\t{y}')
    return y

def bsgs(a,b,p):
    m= math.ceil((p-1)**0.5)
    print(f'm = ceilng of sqr {p-1}, so m = {m}')
    j_dict={}
    for j in range(0,m):
        j_dict[pow(b,j,p)]=j
    print(f'pair ((b^j) % {p} , j) = {j_dict}')
    print(f'use extend euclidean to get inverse of {b} in {p}')
    gcd,b_inverse,y=extended_gcd(b,p)
    print(f'Because,{b}*({b_inverse}) + {p}*({y})={gcd}, and {b_inverse}%{p}={b_inverse%p},')
    b_inverse=b_inverse%p
    print(f'inverse of {b} in {p} is {b_inverse}')
    print(f'Compute {b_inverse}^{m} in {p}')
    print('x\te\ty')
    print(f'{b_inverse}\t{m}\t{1}')
    c=fpa_2(b_inverse,m,p)
    print(f'So {b_inverse}^{m} in {p} = {c}')
    x=a
    for i in range(0,m):
        print(f'When i = {i}, the left side is {a}*{c}^{i} mod {p} = {x},',end=' ')
        if x in j_dict.keys():
            print(f'{x} is in the list!')
            j=j_dict[x]
            print(f'Thus, log{b}({a}) = {i}*{m} + {j} mod {p-1}={(i*m+j)%(p-1)}')
            return (i*m+j)%(p-1)
        else:
            print(f'but {x} is not in the list.')
            x=x*c%p
    return None

a=int(sys.argv[1])
b=int(sys.argv[2])
p=int(sys.argv[3])

print(bsgs(a,b,p))
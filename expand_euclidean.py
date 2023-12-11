import sys

def extended_gcd(a, b):
    if a == 0:
        print(f'{a}\t{b}')
        print(f'{b}={0}*{a}+{1}*{b}')
        return b, 0, 1
    else:
        print(f'{a}\t{b}')
        gcd, x, y = extended_gcd(b % a, a)
        print(f'{gcd}={y - (b // a) * x}*{a}+{x}*{b}')
        return gcd, y - (b // a) * x, x

a=int(sys.argv[1])
b=int(sys.argv[2])
 
gcd, x, y = extended_gcd(a, b)
print('The GCD is', gcd)
print(f'x = {x}, y = {y}')
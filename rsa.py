import math
from math import sqrt
import random

class RSA():
    def fpa_2(self,x,e,m):
        y=int(1)
        while e!=0:
            if e%2==0:
                x=int((x*x)%m)
                e=int(e/2)
            else:
                e=int(e-1)
                y=int((x*y)%m)
        return y


    def findPrimefactors(self,s, n) :
        while (n % 2 == 0) :
            s.append(2)
            n = n // 2
        for i in range(3, int(sqrt(n)), 2):
            while (n % i == 0) :
    
                s.append(i)
                n = n // i
        if (n > 2) :
            s.append(n)
    
    def bsgs(self,a,b,p):
        m= math.ceil((p-1)**0.5)
        print(f'm = ceilng of sqr {p-1}, so m = {m}')
        j_dict={}
        for j in range(0,m):
            j_dict[pow(b,j,p)]=j
        print(f'pair ((b^j) % {p} , j) = {j_dict}')
        print(f'use extend euclidean to get inverse of {b} in {p}')
        gcd,b_inverse,y=self.extended_gcd(self,b,p)
        print(f'Because,{b}*({b_inverse}) + {p}*({y})={gcd}, and {b_inverse}%{p}={b_inverse%p},')
        b_inverse=b_inverse%p
        print(f'inverse of {b} in {p} is {b_inverse}')
        print(f'Compute {b_inverse}^{m} in {p}')
        print('x\te\ty')
        print(f'{b_inverse}\t{m}\t{1}')
        c=self.fpa_2(self,b_inverse,m,p)
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

    def primitive_root_search(self,p):
        q=[]
        self.findPrimefactors(self,q,p-1)
        root_set=[]
        for b in range(2,p):
            flag=True
            for divisor in q:
                if 1 == self.fpa_2(self,b,(p-1)/divisor,p):
                    flag=False
                    break
            if flag:
                root_set.append(b)
                break
        return root_set
    
    def fpa(self,x,e,m):
        print('x\te\ty')
        print(f'{x}\t{e}\t{1}')
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
    
    def extended_gcd(self,a, b):
        if a == 0:
            print(f'{a}\t{b}')
            print(f'{b}={0}*{a}+{1}*{b}')
            return b, 0, 1
        else:
            print(f'{a}\t{b}')
            gcd, x, y = self.extended_gcd(self,b % a, a)
            print(f'{gcd}={y - (b // a) * x}*{a}+{x}*{b}')
            return gcd, y - (b // a) * x, x
    
    def rabin_miller(self,num):
        s = num - 1
        t = 0
        while s % 2 == 0:
            s = s // 2
            t += 1

        for trials in range(5):
            a = random.randrange(2, num - 1)
            v = pow(a, s, num)
            if v != 1:
                i = 0
                while v != (num - 1):
                    if i == t - 1:
                        return False
                    else:
                        i = i + 1
                        v = (v ** 2) % num
        return True


    def is_prime(self,num):
        if num < 2:
            return False
        
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        if num in small_primes:
            return True

        for prime in small_primes:
            if num % prime == 0:
                return False
            
        return self.rabin_miller(self,num)


    def get_prime(self,key_size=1024):
        while True:
            num = random.randrange(2**(key_size-1), 2**key_size)
            if self.is_prime(self,num):
                return num
    
    def factoring(self,x):
        data=[]
        for i in range(2,int(x**1/2)+1):
            if x%i == 0:
                data.append(i)
        return data[0],data[1]

    def AliceGenerateKey(self):
        p=self.get_prime(self,7)
        q=self.get_prime(self,7)
        print(f'p={p},q={q}')
        self.n=p*q
        self.fiN=(p-1)*(q-1)
        print(f'n=p*q={self.n},fiN=(p-1)*(q-1)={self.fiN}')
        self.e=self.get_prime(self,7)
        print(f'public Key e={self.e}')
        gcd,self.d,dd=self.extended_gcd(self,self.e,self.fiN)
        self.d=self.d%self.fiN
        print(f'private key is d={self.d}')

    def BobSendMessage(self,message,publicKey,n):
        self.e=publicKey
        self.n=n
        print(f'{message} mod {self.n}={message%n}')
        self.encryptMessage=self.fpa(self,message,self.e,self.n)
        print(f'encryptMessage={self.encryptMessage}')
    
    def AliceRecieveMessage(self,encryptMessage):
        message=self.fpa(self,encryptMessage,self.d,self.n)
        print(f'decrypt message is {message}')
    
    def Eve(self,encryptMessage,n,e):
        p,q=self.factoring(self,n)
        print(f"p={p},q={q}")
        fiN=(p-1)*(q-1)
        print(f'fiN=(p-1)*(q-1)={fiN}')
        _,d,_=self.extended_gcd(self,e,fiN)
        d=d%fiN
        print(f'private key is d={d}')
        message=self.fpa(self,encryptMessage,d,n)
        print(f'decrypt message is {message}')



rsa=RSA
rsa.AliceGenerateKey(rsa)
rsa.BobSendMessage(rsa,1314,rsa.e,rsa.n)
rsa.AliceRecieveMessage(rsa,rsa.encryptMessage)
rsa.Eve(rsa,rsa.encryptMessage,rsa.n,rsa.e)
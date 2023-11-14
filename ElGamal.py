
import math
from math import sqrt
import random
class ElGamal():
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
    
    def AliceGenerateKey(self,Zp):
        self.Zp=Zp
        root_set=self.primitive_root_search(self,self.Zp)
        self.g=root_set[random.randint(0,len(root_set)-1)]
        print(f"Choose {self.g} as generate root,",end=' ')
        self.x=random.randint(0,self.Zp-1)
        print(f'{self.x} as Alice\'s private key.')
        print(f'g^x:')
        self.gx=self.fpa(self,self.g,self.x,self.Zp)
        print(f'So public key of Alice is (g^x={self.gx},g={self.g},m={self.Zp})')
    
    def BobGenerateKey(self,g,Zp,gx):
        self.g=g
        self.Zp=Zp
        self.gx=gx
        self.y=random.randint(0,self.Zp-1)
        print(f'g^y:')
        self.gy=self.fpa(self,self.g,self.y,self.Zp)
        print(f'So public key of Bob is (g^y={self.gy})')
    
    def AliceSendMessage(self,message):
        print("get (g^y)^x")
        p=self.fpa(self,self.gy,self.x,self.Zp)
        print(f"(g^y)^x={p}")
        self.encryptedMessage=(message*p)%self.Zp
        print(f"encrypt message={(message*p)%self.Zp}")
    
    def BobRecieveMessage(self,encryptedMessage):
        print("get (g^x)^y")
        p=self.fpa(self,self.gx,self.y,self.Zp)
        print(f"(g^x)^y={p}")
        print("get ((g^x)^y)^-1")
        gcd,q,dd=self.extended_gcd(self,p,self.Zp)
        q=q%self.Zp
        print(q)
        print(f"decrypt message={(q*encryptedMessage)%self.Zp}")
    
    def Eve(self,encryptedMessage,g,Zp,gx,gy):
        self.g=g
        self.Zp=Zp
        self.gx=gx
        self.gy=gy
        y=self.bsgs(self,self.gy,self.g,self.Zp)
        print("get (g^x)^y")
        p=self.fpa(self,self.gx,y,self.Zp)
        print(f"(g^x)^y={p}")
        print("get ((g^x)^y)^-1")
        gcd,q,dd=self.extended_gcd(self,p,self.Zp)
        q=q%self.Zp
        print(q)
        print(f"decrypt message={(q*encryptedMessage)%self.Zp}")



        
El=ElGamal
El.AliceGenerateKey(El,101)
El.BobGenerateKey(El,El.g,El.Zp,El.gx)
El.AliceSendMessage(El,77)
El.BobRecieveMessage(El,El.encryptedMessage)
El.Eve(El,El.encryptedMessage,El.g,El.Zp,El.gx,El.gy)

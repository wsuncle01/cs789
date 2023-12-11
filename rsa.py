import math
from math import sqrt
import random
import MillerRabin
import PollardP1
import sympy

class RSA():
    # def fpa(self,x,e,m):
    #     y=int(1)
    #     while e!=0:
    #         if e%2==0:
    #             x=int((x*x)%m)
    #             e=int(e/2)
    #         else:
    #             e=int(e-1)
    #             y=int((x*y)%m)
    #     return y
    
    def fpa(self,p, q, n):
        res = 1
        while q :
            if q & 1:
                res = (res * p) % n
            q >>= 1
            p = (p * p) % n
        return res

    def extended_gcd(self,a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.extended_gcd(self,b % a, a)
            return gcd, y - (b // a) * x, x

    def AliceGenerateKey(self,bit=7):
        p=MillerRabin.largePrime_Generate(bit)
        q=MillerRabin.largePrime_Generate(bit)
        print(f'p={p},q={q}')
        self.n=p*q
        self.fiN=(p-1)*(q-1)
        print(f'n=p*q={self.n},fiN=(p-1)*(q-1)={self.fiN}')
        self.e=MillerRabin.largePrime_Generate(bit)
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
    
    def AliceRecieveMessage(self,encryptMessage,privatekey,group):
        self.d=privatekey
        self.n=group
        message=self.fpa(self,encryptMessage,self.d,self.n)
        print(f'decrypt message is {message}')
    
    def Eve(self,encryptMessage,n,e):
        # p,q=self.factoring(self,n)
        p,q=PollardP1.factor(n)
        # factors=PollardP1.factor(n)
        # p,q=factors,n//factors
        print(f"p={p},q={q}")
        fiN=(p-1)*(q-1)
        print(f'fiN=(p-1)*(q-1)={fiN}')
        _,d,_=self.extended_gcd(self,e,fiN)
        d=d%fiN
        print(f'private key is d={d}')
        message=self.fpa(self,encryptMessage,d,n)
        print(f'decrypt message is {message}')



rsa=RSA
# rsa.AliceGenerateKey(rsa,24)
# rsa.BobSendMessage(rsa,message=1314,publicKey=84739926422245,n=93780358505089)
# rsa.AliceRecieveMessage(rsa,encryptMessage=12694948425761,privatekey=21616331121127,group=106589403545291)
rsa.Eve(rsa,encryptMessage=25600255680903,n=93780358505089,e=84739926422245)
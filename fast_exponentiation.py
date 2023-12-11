import sys

len=len(sys.argv)
x=int(sys.argv[1])
e=int(sys.argv[2])
m=int(sys.argv[3])

def fpa(x,e,m):
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



fpa(x,e,m)

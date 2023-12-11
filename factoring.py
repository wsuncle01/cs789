import sys

len=len(sys.argv)
x=int(sys.argv[1])

data=[]
for i in range(2,int(x**1/2)+1):
    if x%i == 0:
        data.append(i)

print(data)
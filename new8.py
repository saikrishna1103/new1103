import math
s,b=map(int,input().split())
li=list(map(int,input().split()))
p=[]
for i in range(0,b):
    l,r=map(int,input().split())
    p.append([l,r])
for j in p:
    e=j[0]-1
    f=j[1]-1
    print(math.gcd(li[e],li[f]))

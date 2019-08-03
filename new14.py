s,b=map(int,input().split())
p=list(map(int,input().split()))
for i in range(b):
    f,g=map(int,input().split())
    t = p[f-1:g]
    u = t[0]
    for i in range(1,len(t)):
        u = u ^ t[i]
    print(u)

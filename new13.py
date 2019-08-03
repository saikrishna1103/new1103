s,b=map(int,input().split())
p=list(map(int,input().split()))
s=[]
for i in range(b):
    u,v=map(int,input().split())
    s.append(min(p[u-1:v]))
print(*s,sep="\n")

A1,B1=map(int,input().split())
C1=list(map(int,input().split()))
p1=list(map(int,input().split()))
q1=[]
s=0
for i in range(A1):
    x1=p1[i]/C1[i]
    q1.append(x1)
while B1>=0 and len(q1)>0:
    mindex=q1.index(max(q1))
    if B1>=C1[mindex]:
        s=s+p1[mindex]
        B1=B1-C1[mindex]
    C1.pop(mindex)
    p1.pop(mindex)
    q1.pop(mindex)
print(s)

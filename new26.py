s=int(input())
q=list(map(int,input().split()))
a=1
for i in range(0,len(q)-1):
    if q[i]<q[i+1]:
        a+=1
print(a)

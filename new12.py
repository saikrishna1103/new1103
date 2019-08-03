s,b=input().split()
p=list(map(int,input().split()))
for i in range(int(b)):
    u,v=input().split()
    sum=0
    for z in range(int(u)-1,int(v)):
        sum=sum+p[z]
    print(sum)
    continue

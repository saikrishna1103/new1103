s=int(input())
q=list(map(int,input().split()))
n=0

for i in range(0,s):

    for j in range(0,i):
        if q[j]<q[i]:
            n=n+q[j]

print(n)

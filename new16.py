s=int(input())
p=list(map(int,input().split()))
a=[1]*s
for i in range(len(p)):
    if i==0:
        if p[i]>p[i+1]:
            a[i]=a[i]+a[i+1]
    elif i>0:
        if p[i]>p[i-1]:
            a[i]=a[i]+a[i-1]
print(sum(a))

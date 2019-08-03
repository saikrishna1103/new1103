s=int(input())
k=pow(2,s)
w=[]
for i in range(k):  
    m=bin(i).replace("0b","")
    w.append(m.zfill(s))
    w.sort(key=(lambda x:x.count('1')))
for i in w:
    print(i)

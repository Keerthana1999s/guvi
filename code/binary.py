a=int(input())
m=[]*a
for i in range(0,2**a):
    k=[]
    for j in range(a-1,0,-1):
        k.append(int(i/2**j)%2)
    k.append(i%2)    
    m.append(k) 
    
for i in  m:
    s=''
    for j in i:
        j=str(j)
        s=s+j
    print(s)

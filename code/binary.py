n=int(input())
m=[]*n
for i in range(0,2**n):
    a=[]
    for j in range(n-1,0,-1):
        a.append(int(i/2**j)%2)
    a.append(i%2)    
    m.append(a) 
    
for i in  m:
    s=''
    for j in i:
        j=str(j)
        s=s+j
    print(s)



   
     
  

    


  
     



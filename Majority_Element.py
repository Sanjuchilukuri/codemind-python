def doo(l,k):
    for i in l:
        
        if l.count(i)>=k:
            return i
            
        
    
import math  
n=int(input())
l1=list(map(int,input().split()))
l=l1
k=int(math.ceil(n/2))
print(doo(l,k))

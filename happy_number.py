#from SANJU
def Happy(n):    
    rem=sum=0;    
    while(n>0):    
        rem=n%10;    
        sum=sum+(rem*rem);    
        n=n//10;    
    return sum;    
n=int(input())   
temp=n    
while(temp!=1 and temp!=4):    
    temp=Happy(temp);    
if(temp==1):    
    print("True")   
elif(temp==4):    
    print("False")
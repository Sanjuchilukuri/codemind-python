n=int(input())
k=list(map(int,input().split()))
c=0
for i in range(n):
    if(k[i]%2==0):
        if(i%2==0):
            c+=1
        else:
            print("False")
            break
else:
    print("True")
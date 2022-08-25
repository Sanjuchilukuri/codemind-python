t=int(input())
while(t):
    s=input()
    k=0
    for j in s:
        if (j.isdigit()):
            k=1
    if k==1:
        print("Yes")
    else:
        print("No")
    t-=1
def ispalin(s):
    k=s[::-1]
    if(s==k):
        return True
    else:
        return False



t=int(input())
while(t):
    n=input()
    if(ispalin(n)):
        print(True)
    else:
        print(False)
    t-=1
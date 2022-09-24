n=int(input())
l=list(map(int,input().split()))
if n%2==0:
    print(*l)
else:
    l.append(0)
    print(*l)
n=input()
l=[]
for i in n:
    l.append(int(i))
for i in range(len(l)):
    if l[i]==6:
        l[i]=9
        break
for i in l:
    print(i,end="")
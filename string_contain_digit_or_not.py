s=input()
k=0
for j in s:
    if (j.isdigit()):
        k+=1
if k>0:
    print("Contains",k,"digit")
else:
    print("Doesn't contain digit")
    
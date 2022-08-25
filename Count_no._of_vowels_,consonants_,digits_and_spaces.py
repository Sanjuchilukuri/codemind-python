c=0
d=0
w=0
v=0
n=input()
v1=['a','e','i','o','u','A','E','I','O','U']
for i in n:
    if i.isdigit()==1:
        d+=1
    elif i==" ":
        w+=1
    elif i in v1:
        v+=1
    else:
        c+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)
s1=input()
s2=input()
s3=s1+s2
l=list(s3)
l.sort()
s5=""
for i in l:
    s5+=i
print(s5)
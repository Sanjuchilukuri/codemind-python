
l=list(map(int,input().split(" ")))
hf=l[0]
sf=l[1]
spf=l[2]
if(hf>50 and sf>60 and spf>100):
    print("10")
elif(hf>50 and sf>60 and spf<100):
    print("9")
elif(hf<50 and sf>60 and spf>100):
    print("8")
elif(hf>50 and sf<60 and spf>100):
    print("7")
elif( hf>50 or sf>60 or spf>100):
    print("6")
else:
    print("5")
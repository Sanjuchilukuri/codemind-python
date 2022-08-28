l=int(input())
n=int(input())
while(n):
    w,h=map(int,input().split())
    if(w<l or h<l):
        print("UPLOAD ANOTHER")
    elif(w==h):
        print("ACCEPTED")
    else:
        print("CROP IT")
    n-=1
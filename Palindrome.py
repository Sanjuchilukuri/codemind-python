def ispalin(n):
    k=n[::-1]
    return n==k
n=input()
print(ispalin(n))
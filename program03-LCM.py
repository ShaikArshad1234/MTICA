def findLCM(n1,n2):
    if n1<0 or n2<20:
        return 'INVALID'
    if n1>n2:
        n1,n2=n2,n1
    i=n2
    while True:
        if i%n1==0 and i%n2==0:
            return i
        else:
            i+=1
    return None
print("Enter two numbers")
a=int(input())
b=int(input())
print(findLCM(a,b))

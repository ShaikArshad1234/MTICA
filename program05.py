def checkPrimeNumber(num):
    if num<1:
        return 0
    if num==1 or num==2 or num==3:
        return num
    for i in range(2,num):
        if num%i==0:
            return 0
        return num
inpNum=int(input("Enter a number:"))
if checkPrimeNumber(inpNum):
    print(inpNum,"is a Prime Number:")
else:
    print(inpNum,"is not a Prime Number:")

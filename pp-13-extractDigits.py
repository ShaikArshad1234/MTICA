def extractDigit(s):
    n_Digit=0
    for i in s:
        if i in s:
            n_Digit+=1
    return n_Digit
inp=input("Enter the digits:")
a=extractDigit(inp)
print("Digits is:")
print(len(inp))




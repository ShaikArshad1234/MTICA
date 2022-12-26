def countNumber(a):
    n_num=0
    for i in a:
        if i in a:
            n_num+=1
    return n_num
inpNum=input("Enter the Number:")
s=countNumber(inpNum)
print("No.of Number is")
print(len(inpNum))

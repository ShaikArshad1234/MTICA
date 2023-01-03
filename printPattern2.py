def printS(ch,n):
    Num="."
    for i in range(0,n):
        print(Num*(n-i-1)+ch*(2*i+1)+Num*(n-i-1))
    return None
inpch=input()
inpNum=int(input())
printS(inpch,inpNum)

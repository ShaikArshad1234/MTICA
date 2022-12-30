def printSeries(ch,n):
    s=' '
    for i in range(0,n):
        print(s*(n-i-1) +ch*(2*i+1)+s*(n-i-1))
    return None
inpch=input()
inpNum=int(input())
printSeries(inpch,inpNum)

def  printSeries(ch,n):
    assert isinstance(ch,str)
    assert isinstance(n,int)
    for i in range(n,0,-1):
        print(ch*i)
    return None
inp=input("Enter a ch:")
inpNum=int(input("Enter a no:"))
print('-'*40)
try:
    printSeries(inp,inpNum)

except AssertionError as a:
    print(a)

##inp=input("Enter a ch:")
##inpNum=int(input("Enter a no:"))
##printSeriesIncreasing(inp,inpNum)
##print('-'*40)
##printSeriesDecreasing(inp,inpNum)
##

def  printSeries(n):
    num=1
    
    for i in range(1,n+1):
        print()
        for j in range(i):
            print(i,end=' ')
            num+=i
            
    return None
n=int(input())
printSeries(n)



    

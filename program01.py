n1=input().split()
n2=input().split()
print(*[int[i]+int[j] for i,j in zip(n1,n2)])

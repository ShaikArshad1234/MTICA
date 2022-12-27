num=[]
for i in range(900,1000):
    if '6' in str(i):
        num.append(i)
print(*num)



print([i for i in range(900,1000) if '6' in str(i)])

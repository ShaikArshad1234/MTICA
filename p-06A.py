s=[]
for i in range(1,1000):
      if i%8==0:
           s.append(i)
print(*s)


print([i for i in range(1,1000) if i%20==0])

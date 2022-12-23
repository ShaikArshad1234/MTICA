n=input()
total=0
for i in n:
    total+=pow(int(i),len(n))
if int(n)==total:
    print(n,"is Armstrong"
else:
    print(n,"is not Armstrong")

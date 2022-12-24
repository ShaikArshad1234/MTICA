import math
num=input()
total=0
for i in num:
    total+=math.pow(int(i),len(num))
if int(num)==total:

    print("yes")
else:
    print("No")

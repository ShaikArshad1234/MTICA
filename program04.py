rev=0
n=786
while(n):
    rev=rev*10+n%10
    n=n//10
print(rev)

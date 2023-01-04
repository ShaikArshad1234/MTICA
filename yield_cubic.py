def calcubic():
    i=1;
    while True:
        yield i*i*i
    
        i+=1
for num in calcubic():
    if num>1000:
        break
    print(num)

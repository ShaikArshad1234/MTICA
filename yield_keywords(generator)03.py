def squares(x=0):
    while x<10:
        x=x+1
        yield x*x
##yeildedList=[i for i in squares()]
##print(yeildedList)


yieldedList=list(squares())
print(yieldedList)

def fun(str1):
    print(str1)
    return
fun("I am first call to user defined function!")
fun("Again second call to the same function")

def printMe(str1,n):
    n[-2]='Arshad'
    print(str1,n)
    return

x=['Prathap','Arun','Prathap']
printMe("Wakeup",x)
print("x:",x)

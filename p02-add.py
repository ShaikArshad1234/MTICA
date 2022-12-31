def add(*n):
    temp=0
    for i in n:
        temp+=i
    return temp
print("add():",add())
print("add(5):",add(5))
print("add(5,7):",add(5,7))
print("add(5,7,2):",add(5,2,7))
print("add(5,7,2,11,55,77):",add(5,7,2,11,55,77))

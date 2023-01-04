
x=5;y=7
def changeMe(mylist):
    "This function demostrates local and global variables"
    p=89
    global x,y
    x=y+2
    mylist=[1,2,3,4]
    print("values inside the function:",mylist)
    print("local variable are:",locals())
    print("global variables are:",globals())
    return
mylist_var=[10,20,30]
changeMe(mylist_var)
print("values outside the function:",mylist_var)

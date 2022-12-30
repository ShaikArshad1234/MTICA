def printDay(dn):
    if(dn==1):
        return "Monday"
    elif(dn==2):
        return "Tuesday"
    elif(dn==3):
        return "Wednesday"
    elif(dn==4):
        return "Thursday"
    elif(dn==5):
        return "Friday"
    elif(dn==6):
        return "Saturday"
    elif(dn==7):
        return "Sunday"
    else:
        return "Invalid"
import time
for i in range(3):
    inpNum=int(input())
    start=time.time()
    print(printDay(inpNum))
    print(time.time()-start)

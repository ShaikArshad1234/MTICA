class Number:
    def __init__(self,number):
        self.number=number
    def checkEven(self):
        if self.number%2==0:
            return "Even"
        else:
            return "Odd"
    def sumDigits(self):
        if self.number<0:
            self.number=abs(self.number)
        temp=str(self.number)
        total=0
        for i in temp:
            total+=int(i)
        return total
    def checkArmstrong(self):
        t=0
        for i in num:
            t+=pow(int(i),len(n))
        if int(num)==t:
            return "armstrong"
        else:
            return "not"
    def calculateFactorail(self):
        if self.number==0:
            return 1
        res=1
        for i in range(1,self.number+1):
            res*=i
        return res



num=int(input())
ob=Number(num)
print('checkEven',num,'is',ob.checkEven())
print('sumDigits',num,'is',ob.sumDigits())
print('checkArmstrong',num,'is',ob.checkArmstrong())
print('Factorail of',num,'is',ob.calculateArmstrong())

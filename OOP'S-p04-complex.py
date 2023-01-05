class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __sub__(self,ob):
        temp=self.real-ob.real,self.img-ob.img
        return temp
    def __add__(self,ob):
        temp=self.real+ob.real,self.img+ob.img
        return temp
    def __mul__(self,ob):
        temp=(self.real*ob.real-self.img*ob.img,
              self.real*ob.img+self.img*ob.real)
        return temp

    def __str__(self):
        return(self.rael,self.img)

ob1=Complex(3,5)
ob2=Complex(2,1)
ob3=ob1+ob2
ob4=ob1-ob2
ob5=ob1*ob2
print(ob3)
print(ob4)
print(ob5)

    

class circle:
    pi=22/7
    def __init__(self,radius):
        self.radius=radius
    def calArea(self):
        temp=self.pi*self.radius**2
        return temp
    def calPerimeter(self):
        temp=2*self.pi*self.radius
        return temp
r=int(input())
ob=circle(r)
area=ob.calArea()
peri=ob.calPerimeter()
print('Area of circle with radius',r,'is',area)
print('Perimeter of circle with radius',r,'is',peri)

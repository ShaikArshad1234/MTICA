class Vehicle:
    def __init__(self,max_speed,mileage):
        self.mileage=mileage
        self.max_speed=max_speed

modelX=Vehicle(240,18)
print(modelX.max_speed,modelX.mileage)

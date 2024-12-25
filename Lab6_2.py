class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def get_info(self):
        return "Марка : {} Модель : {} ".format(self.make,self.model)
class Car(Vehicle):
    def __init__(self,make,model,fuel_type):
        super().__init__(make,model)
        self.fuel_type = fuel_type
    def get_info(self):
        return super().get_info() + "Тип топлива : {} ".format(self.fuel_type)
v=Vehicle('Toyota','aqua')
print(v.get_info())
c=Car('Toyota','aqua','petrol')
print(c.get_info())

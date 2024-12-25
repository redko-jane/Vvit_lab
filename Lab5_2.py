class circle:
    def __init__(self,radius):
        self.radius=radius
    def get_radius(self):
        return "Радиус круга : {}".format(self.radius)
    def set_radius(self,new_radius):
        self.radius=new_radius
c=circle(45)
c.set_radius(71)
print(c.get_radius())

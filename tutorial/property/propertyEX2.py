class circle:
    def __init__(self, radius):
        self.__radius=radius
        self.__diameter=2*radius
        self.__area=str(radius**2)+'π'
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,radius):
        self.__radius=radius
    @property
    def diameter(self):
        return self.__radius*2
    @property
    def area(self):
        return str(self.__radius**2) +'π'
a= circle(6)
a.radius=7
print(a.radius)
print(a.diameter)
print(a.area)

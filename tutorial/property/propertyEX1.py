class test:
    def __init__(self):
        self._name="JM"
        self._number="12"
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name

a= test()
print(a.name)
a.name= 'hg'
print(a.name)

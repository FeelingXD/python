class Robot:
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduce_self(self):
        print("my name is "+self.name) #java style

#r1 = Robot()
#r1.name ="Tom"
#r1.weight =30
#r1.color= "red"

#r2= Robot()
#r2.name = "Jerry"
#r2.color = "blue"
#r2.weight = 40

r1 =Robot("Tom","red",30)
r2 =Robot("Jerry","blue",45)

class Person :
    def __init__(self,n,p,i):
        self.name=n
        self.personality=p
        self.is_sitting =i

    def sit_down():
        self.is_sitting=True
    def stand_up():
        self.is_sitting=False

p1= Person("Alice","aggresive",False)
p2= Person("Becky","talkative",True)

p1.robot_owned=r2
p2.robot_owned=r1

p1.robot_owned.introduce_self()

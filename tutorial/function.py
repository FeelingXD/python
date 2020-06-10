def function1():
    print("ahhh")
    print("ahhh2")

print("this is out of function1 line")
function1()
def function2(x):
    return x*2
a=function2(10)
print(a)

def function3(x,y):
    return x+y
b=function3(1,2)

print(b)

def funtion4(x):
    print(x)
    print("still in funtion")
    return 3*x
f=funtion4(4)
print(f)

def funtion5(x):
    print(x)
    print("weee")
funtion5(4)
#BMI calculator

name1 ="YK"
height_m1 =2
weight_kg1 =90

name2 ="YK sister"
height_m2 =1.8
height_kg2=70

def bmifunction(name,height_m,weight_kg):
    bmi = weight_kg/(height_m**2)
    print("bmi: ")
    print(bmi)
    if bmi<25 :
        return name +" not overweight"
    else:
        return name +"is overweight"

result1 =bmifunction(name1 ,height_m1,weight_kg1)
print(result1)

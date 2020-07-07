a=[1,3,5,7,9,11]

b=[]
b.append(10)
b.append(20)
print(b)
c= []
for x in a:
    c.append(x*2)
print(c)
d=[x*2 for x in a]
print(d)
e2 =[x**2 for x in range(1,7)]
print(e2)

for x in  range(6,0,-1):
    print(x)

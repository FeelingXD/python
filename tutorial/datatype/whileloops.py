#while loop and break statement UwU
total =0
for i in range(1,5):
    total +=i
print(total)

total2=0
j =1
while j<5:
    total2 +=j
    j+=1
print(total2)

given_list =[5,4,4,3,1]

total3 =0
i=0

while i<5 and given_list[i]>0:
    total3+=given_list[i]
    i+=1
print(total3)

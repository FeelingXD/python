ls =[22,10,25,7,9,30,12,19,2,31]
evenindex_list=[0,0,0,0,0]
oddindex_list=[0,0,0,0,0]
result=[0,0,0,0,0]
k=0
for i in range(0,10,2):
    evenindex_list[k]=ls[i]
    k+=1
k=0
for i in range(1,10,2):
    oddindex_list[k]=ls[i]
    result[k]= evenindex_list[k] - oddindex_list[k]
    k+=1
print(evenindex_list)
print(oddindex_list)
print(result)

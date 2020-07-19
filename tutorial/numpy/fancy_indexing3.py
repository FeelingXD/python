import numpy as np

a= np.array([0,1,2,3,4,5,6,7,8])
integer_index = np.array([0,2,5,6])
bool_index = np.array([True, False,False,True,False,True,True,True,False])
#print(a[integer_index])
print(np.take(a,integer_index))

#print(a[bool_index])
print(np.compress(bool_index,a))

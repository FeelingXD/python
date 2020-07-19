import numpy as np

a = np.array([0,1,2,3,4,5,6,7,8])
index=np.array([1,4,5])
print(a[index])

b= np.array([[0,1,2],[3,4,5],[6,7,8]])
index = np.array([0,2])
index2 = np.array([1,2])
print(b[index,index2])
print(index, index2)
print(b[[1,2]])

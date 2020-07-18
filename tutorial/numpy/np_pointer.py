import numpy as np
# numpy 인덱싱은 동일한 영역 메모리를 할당
a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
a_view = a[0:1]
a_view[0] = [9, 10, 11]
print(a)
a[0]=[0,1,2]
print(a_view)

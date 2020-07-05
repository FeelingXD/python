# unique 알고리즘 . 중복제거
key=[]
for i in range(1,51):
    key.append(i)
    key.append(i)
key=list(set(key))
print(key)

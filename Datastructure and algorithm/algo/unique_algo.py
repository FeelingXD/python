# unique 알고리즘 . 중복제거
# set 을 이용 한 제거 set은 순서는 상관없으나 중복 하지않음

key=[]
for i in range(1,51):
    key.append(i)
    key.append(i)
key=list(set(key))
print(key)

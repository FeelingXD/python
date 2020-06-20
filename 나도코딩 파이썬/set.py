#set 자료형  집합 ex  중복이 안되고 , 순서가 없음

my_set={1,2,3,3,3}
print(my_set)

java ={'유재석','조세호','박명수'}
python ={'유재석','이명수'}

# 교집함 출력하기
print(java & python)  # and 로는 사용이 안된다. :/
print(java.intersection(python)) # 동일한 기능을한다.

# 합집합
print(java | python) # java 혹은 python
print(java.union(python)) # 동일한 기능을 한다.

# 차집합
print( java- python)
print(java.difference(python))

# 추가하기
java.add('김태호')
print(java)
# 제거하기
java.remove('김태호')
print(java)

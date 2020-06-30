#dictionary
cabinet={3:"유재석",100:"조세호"} # 중괄호로 dictionary 선언
print(cabinet)
print(cabinet[3]) # 3의키값과 대응되는 유재석 반환

print(cabinet.get(3))
print(cabinet.get(5))# 키값과 대조하여 값을 반환 없을경우 none 반환
print(cabinet.get(5,"트릭시"))# 임시로 값

# 새로 입력하기
print(cabinet)
cabinet["a-3"]= "김종국"
cabinet["c"]= "서현"
print(cabinet)

# 목록 지우기
del cabinet['a-3']
print(cabinet)

# key만 출력
print(cabinet.keys())
#value 출력
print(cabinet.values())

#key : value 쌍출력
print(cabinet.items())

# 클리어
cabinet.clear()
print(cabinet)

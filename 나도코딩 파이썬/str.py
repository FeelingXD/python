python= 'Python is Amazing'

print(python.lower())# 대문자 소문자변환
print(python.upper())# 소문자 대문자변환

print(python[0].isupper())# 첫글자가 대문자인지 확인
print(len(python))# python 문자열의 길이출력

print(python.replace('Python','Java'))# 문자열 변경
index = python.index('n') # 처음 발견하는 n 위치값 반환
print(index)

index = python.index('n',index + 1)
print(index)

print(python.find("Java"))
print("HI")

print(python.count('n'))

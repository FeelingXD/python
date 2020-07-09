myString ='Monty Python'
print(myString[0:4])
print(myString[2:4])
print(myString[4:8])
print(myString[2:5])
print(myString[1:7])# str 저장값은 문자(배열 )형태로 저장되며 [0:n-1]까지 표시

#문자열 합치기
first_str="hello"
second_str="There"
print(first_str+second_str)
third_str=first_str+' '+second_str
print(third_str)

#in 논리인자로 사용하기
fruit= 'banana'

print('n' in fruit) # bool 값으로 참 거짓을 판별함
print('nan' in fruit) # 연속된 여러단어도 가능

if 'a' in fruit:
    print("found it ! ")# if 형으로 조건식으로도 사용가능함
#문자열 라이브러리
greet = 'Hello !'
zap = greet.lower() # 대문자를 소문자로 변경
print(zap)
print("Hello Bob".lower()) # 함수형이므로 괄호를 반드시 포함한다.

print(zap.upper()) # lower와 반대의 upper 함수도 있음

#공백제거 함수 strip
greet= "        hello    :0     "
print(greet.lstrip()) # left strip 왼족 공백제거
print(greet.rstrip())# right strip 오른쪽 공백제거
print(greet.strip())# 양쪽 공백 제거
#시작문자열 찾기  startswith start str with 의 줄인말인거같다.

line = 'Please have a nice day'
print(line.startswith('Please'))# bool 값으로 참거짓 판별
print(line.startswith('p'))# 대소문자를 구분한다.
print(line.startswith('p'.upper())) #upper로 형지정을해도 ok

str ='X-DSPM-Confidence: 0.8475'

ipos = str.find(':')
piece = str[ipos+2:]
value =float(piece)
print(value)

value = '*'
print(value:2)

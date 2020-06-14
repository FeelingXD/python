
# % 를이용하여 값할당하기
print("나는 %d 살입니다." % 20)
print("나는 %s를 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요" %"A")
print("나는 %s 색과 %s 색을 좋아해요" %("빨강", "파랑"))

# format 을 사용하여 값할당하기
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("빨강",'파랑'))
print("나는 {1}색과 {0}색을 좋아해요".format("빨강",'파랑')) # 값을 지정할수잇다.

print("나는 {age}살 이며 {color}색을 좋아해요".format(age=20,color="빨강"))
age =20
color ="파랑"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

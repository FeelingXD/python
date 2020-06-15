# waint num

for waiting_no in{0,1,2,3,4}:
    print("대기번호:{0}".format(waiting_no))


# 문자도 사용가능 (리스트)

starbucks =["아이언맨","토르","아이엠 그루트"]

for customer in starbucks:
    print("{0} , 커피가 준비되었습니다.".format(customer))

customer = "토르"

index =5

while index>=1:
    print("{} ,커피가 준비되었습니다. {}번 남앗어요".format(customer,index))
    index-=1

person ="unknown"
'''
while person !=customer:
    print("{}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? :")
'''
absent =[2,5]
for student in range(1,11): # 1~10
    if student in absent:
        continue
    print("{},책을 읽어봐".format(student))

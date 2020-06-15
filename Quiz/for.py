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
no_book=[7]
for student in range(1,11): # 1~10
    if student in absent:
        continue  # 건너뛰고 다음 번호 실행
    elif student in no_book:
        print("오늘수업은 여기까지 {}은 교무실로".format(student))
        break
    print("{},책을 읽어봐".format(student))

# 한줄로 작성하는 for 문

students = [i for i in range(1,11)]
print(students)

fruits = ["banana","apple"]
fruits = [i.upper() for i in fruits]
print(fruits)

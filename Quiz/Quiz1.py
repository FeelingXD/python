"""Quiz . 당신의 학교는 학교에서 파이썬 코딩대회를 주최합니다.
참석률을 높이기위해 댓글 이벤트를  진행하기로   하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은  커피 쿠폰을 받게됩니다.
추첨 프로그램을 작성하시오

조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건 2 : 댓글 내용과 상관 없이  무작위로 추첨하되  중복 불가
조건 3 : random 모듈의 shuffle과 sample 활용

출력 예제
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : 2, 3, 4
-- 축하합니다. --

"""
from random import *
users = list(range(1,21)) # 20명 선언
print(users)
winners = sample(users,4)
firstwinner = sample(winners,1)
winners =list(set(winners) - set(firstwinner))
def print_winner(a,b):
    print("-- 당첨자 발표 --")
    print(f'치킨당첨자 : {a} ' )
    print(f'커피당첨자 : {b}')
    print("-- 축하합니다. --")

print_winner(firstwinner,winners)

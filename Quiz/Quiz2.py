'''
당신은 cocoa 서비스를 이용하는 택시 기사입니다.'
50명의 승객과 매칭 기회가 있을때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1 : 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수입니다.
조건 2 : 당신은 소요시간 5~15분 사이의  승객만 매칭해야합니다.

출력문 예제
[o] 1번째 손님 (소요시간 :15분 )
[] 2번째 손님 (소요시간 : 50분 )
. .


총탑승 승객 : 1 분
'''
from random import *
cnt = 0
passenger =[x for x in range(1,51)]
for i in passenger :
    time = randrange(5,51)  # 소요시간 함수
    if 5<=time<=15:
        print("[O] {}번째 손님 (소요시간 {}분)".format(i,time))
        cnt+=1
    else:
        print("[] {}번째 손님 (소요시간 {}분)".format(i,time))
print(f'총탑승 승객 : {cnt}분')

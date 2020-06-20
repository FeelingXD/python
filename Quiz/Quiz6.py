'''
Quiz) 동네에서 항상 대기 손님이 있는 치킨 집이있다.

대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 개발하려한다.
시스템 코드의 적절한 예외 구문 을 넣으시오

조건1 : 1보다 작거나 숫자가 아닌 입력이 들어오면 ValueError 로 처리한다.
        출력 메세지 : 잘못된값을 입력하셧습니다.
조건2 : 대기 손님이 주문할수있는  총 치킨량은 10마리 로 한정
        치킨 소진시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램을 종료
        출력 메세지 : "재고가 소진되엇습니다. 더이상 주문을 받지않습니다."

[코드]
'''
class SoldOutError(Exception):
    pass


chicken = 10
waiting = 1 #홀 안은 만석  대기번호는 1번부터 시작
while (True):
    try:
        print("[남은치킨]: {}".format(chicken))
        order = int(input('치킨을 몇 마리 주문 하시겠습니까? :'))
        if order>chicken :
            print("재료가 부족합니다. :()")
        elif order<=0:
            raise ValueError
        else :
            print('[대기번호 {}] 주문 이 완료되엇습니다. XD'.format(waiting,order))
            waiting +=1
            chicken -=order
        if chicken ==0 :
            raise SoldOutError
    except ValueError :
            print('잘못된 값을 입력하셧습니다.')
    except SoldOutError :
            print('제고가 소진되었습니다.더이상 주문을 받지않습니다')
            break

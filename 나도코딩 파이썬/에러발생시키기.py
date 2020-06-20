# 사용자 정의 에러 만들기
class BigNumberError(Exception): # exception 클래스를 상속한 새로운 에러
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
try:
    print('한자리 숫자 나누기 전용 계산기 입니다.')
    num1 = int(input('첫번째 숫자를 입력해주세요'))
    num2 = int(input('두번째 숫자를 입력해주세요'))
    if num1>=10 or num2>=10:
        raise BigNumberError('입력값 : {}, {}'.format(num1,num2))
    print('{}/{}={}'.format(num1,num2,num1/num2))
except ValueError:
    print('잘못된 값을 입력하셧습니다.')
except BigNumberError as err:
    print("에러가 발생햇습니다.")
    print(err)
finally :
    print("계산기를 이용해주셔서 감사합니다.")# finally 예외가 되건 안되건 무조건 실행을 하는 공간

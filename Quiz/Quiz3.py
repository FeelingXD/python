'''Quiz)  표준 체중을 구하는 프로그램을 작성하시오.

*표준 체중  : 각 개인의 키에 적당한 체중

(성별에 따른공식)
남자 :키 x 키 x 22
여자 : 키 x 키 x 21

조건 1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달 : 키(height), 성별(gender)

조건 2 : 표준 체중은 소숫점 둘째자리까지 표기

(출력 예제)
키 175cm 남자의 표준  체중은  67.38kg 입니다.
'''

def solution(height,gender):
    height=height/100

    if gender=="여자": #female
        std_weight=height*height*21
    else:
        std_weight=height*height*22

    print(f'키 {height} {gender}의 표준 체중은 %.2f kg 입니다.' % std_weight)

solution(175,'남자')

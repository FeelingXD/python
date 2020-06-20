try:
    print('나누기 전용 계산기입니다.')
    nums=[]
    nums.append(int(input('첫번째 숫자를 입력해주세요 :')))
    nums.append(int(input('두번째 숫자를 입력해주세요 :')))
    #nums.append(nums[0]/nums[1])
    print('{}/{}= {}'.format(nums[0],nums[1],nums[2]))
except ValueError: # 값에러
    print('잘못된 값을 입력하셧습니다.')
except ZeroDivisionError as err: #0으로 나눈경우 에러
    print(err)
except Exception as err: #exception 모든 에러
    print('알수없는 에러가 발생하엿습니다.')
    print(err)

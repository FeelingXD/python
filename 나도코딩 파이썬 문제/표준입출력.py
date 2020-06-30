print('python' , 'java' ,sep = ' vs ')  # sep 함수로 인자들간 사이에 어떤것으로 나눌지 정한다


import sys

print('python','java', file=sys.stdout)


 # 시험 성적

scores ={"수학":0 , "영어":50,"코딩":100}
for subject, score in scores.items():
     print(subject.ljust(8), str(score).rjust(4), sep =' : ' , end = " 점 \n")     #just 공간확보 ljust 왼쪽 정렬으로 8칸 공간확보

# 은행 순번 대기표
# 001 ,002 .. ..
for num in range(1,21):
    print('대기번호  : '+ str(num).zfill(3)) # zfill  x 만큼 공간을 확보하고 빈칸만큼 0을채워넣음 zero zfill

answer = input('아무값이나 입력하세요 : ')
print(type(answer))
print('입력하신값은 ' + answer +' 입니다. ')

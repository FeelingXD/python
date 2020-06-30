#glob 경로 내의 폴더 /파일 목록 조회 (윈도우 dir)
'''
import glob
print(glob.glob("*.py"))# .py인 모든파일
'''
#os  운영체제에서 제공하는 기본기능
'''
import os

print(os.getcwd())# 현재 디렉토리

folder ="sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
else   :
    os.makedirs(folder)#폴더 생성
    print(folder , "폴더를 생성하엿습니다.")

print(os.listdir())# 현재폴더 파일목록
'''
'''
import time #시간관련 함수
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
'''
import datetime # 날자 함수
print('오늘 날짜는 ,' ,datetime.date.today())

# time delta : 두 날짜의 간격

today =datetime.date.today()
td =datetime.timedelta(days=100) #100저장
print('100일후 날짜는 {}',today+td)

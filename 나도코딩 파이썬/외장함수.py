#glob 경로 내의 폴더 /파일 목록 조회 (윈도우 dir)
'''
import glob
print(glob.glob("*.py"))# .py인 모든파일
'''
#os  운영체제에서 제공하는 기본기능
import os
print(os.getcwd())# 현재 디렉토리

folder ="sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
else   :
    os.makedirs(folder)#폴더 생성
    print(folder , "폴더를 생성하엿습니다.")

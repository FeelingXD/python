# pickle 모듈 사용
#pickle.py가 있기에 pickle 이라고 py를 만들면 안되요 ^ㅅ^
#profile_file = open("profile.pickle","wb")
#profile ={"이름":"박명수","나이":30 ,"취미":["축구",'골프','코딩']}
#print(profile)

#pickle.dump(profile, profile_file)
#profile_file.close()
'''
import pickle

profile_file = open("profile.pickle",'rb')
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
'''
'''
# with
import pickle

with open("profile.pickle","rb") as profile_file:  # with 문 종료시 자동으로 파일을 닫는다.
    print(pickle.load(profile_file))
'''
'''
with open('study.txt','w',encoding='utf8') as study_file:
    study_file.write('파이썬 공부중')
'''
'''
with open('study.txt','r',encoding='utf8') as study_file:
    print(study_file.read())
'''

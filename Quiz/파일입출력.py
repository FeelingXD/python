#score_file =open("score.txt","w",encoding="utf-8")
#print("수학 : 0",file=score_file)
#print("영어 : 50", file=score_file)
#score_file.close()
''' # 한줄씩읽기
score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
'''
'''# 반복문으로 읽어오기
score_file = open("score.txt", "r", encoding='utf-8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()
'''
score_file = open("score.txt", "r",encoding='utf8')
lines = score_file.readline()# list형으로저장
for line in lines:
    print(line,end="")

score_file.close()

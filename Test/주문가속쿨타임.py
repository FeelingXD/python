# 주문가속 계산기 입니다.
def Skill_ec(raw_cool,excel_score): #분당 스킬사용횟수
    return round(float(100*raw_cool/(100+excel_score)),2)

print('기존 스킬 쿨타임 :')
raw= int(input())
print('스킬 가속 수치 : ')
ex = int(input())
print('감소된 쿨타임 :' , Skill_ec(raw,ex))
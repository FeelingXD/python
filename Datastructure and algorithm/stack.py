# stack datastructure F.I.L.O
class stack:
    def __init__(self):
        self.items=[] #초기화
    def push(self,item):
        self.items.append(item) #추가
    def pop(self):
        return self.items.pop() #제거
    def seek(self):
        return self.items[-1] #마지막원소보기
    def isEmpty(self):
        return not self.items #빈스택인지 확인하기 bool 값으로 비어있으면 True 반환

stk = stack()   #stack 객체 생성
print(stk)      #stack 출력 빈값 object 생성확인
print(stk.isEmpty())
stk.push(1)
stk.push(2)
print(stk.items)
print(stk.seek())
stk.pop()
print(stk.seek())

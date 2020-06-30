#list 개념잡기

#지하철 칸별로 10,20,30

subway =[10,20,30]

print(subway)

subway = ["유재석","조세호","박명수"]
print(subway.index("조세호")) # index 위치값 반환 리스트 배열 은 0값부터 시작

subway.append("하하") # append 리스트에 새로운 값 추가
print(subway)

subway.insert(1,"정형돈 ")# index 1번자리에 값을 할당함 기존 값들은 한칸씩 밀림
print(subway)

subway.pop() # 리스트 가장 뒤의값을 꺼냄

#같은 값 이 몇개인지 확인하기

subway.append('유재석')
print(subway.count('유재석'))

numlist =[5,6,3,5,2]
numlist.sort() # 정렬
print(numlist)
numlist.reverse()
print(numlist) # 역순

numlist= [5,4,3,2,1]
mixlist= ["조세호",11, True]
numlist.extend(mixlist)
print(numlist)

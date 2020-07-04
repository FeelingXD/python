x = str("hello World")#str 문자열 타입
y = int(20) #
z = float(20.5) #
x = complex(1j) #복소수
x = list(("1","2","3",4)) #list 순서가있는 원소집합 [ ] 로도 사용가능
x = tuple(("1","2")) #tuple 읽기전횽 list 또 []로는 사용할수없음 .
x =range(0,6) # default 0 스타트 x 미만 range; for 과 함께 반복문에 사용할수있음
x = dict(name="john",age=36)# hash 와 비슷 한개념 키값에 대조되는 값을 반환 하는데 . 추가공부가 필요
s1 =set([1,2,3])# Set 자료형 집합형 자료형  * 중복을 허용하지않고 *순서를 신경쓰지않는다.
s2 =set("hello")
x = frozenset(("apple", "banana", "cherry"))#set 과 마찬가지인 집합형 자료형이지만 자료 원소를 추가하거나 제외할수없다. (불변형) 하지만 딕셔너리 키 또는 다른집합의 원소로 사용가능
x = bool(5) #bool 비교형 연산자 괄호 안의 내용이 참일경유 True 아닐경우 false 반환 .
x = bytes(5) #byte 자료형 추가공부 필요
x = bytearray(5) #바이트 배열형  바이트와 큰차이는 없으나 요소를 변경할수있다.
x = memoryview(bytes(5))# 메모리뷰 메모리 저장이아닌 중간단계 버퍼에 저장함 연산속도에서 이점이 있음 또 버퍼 데이터를 수정가능

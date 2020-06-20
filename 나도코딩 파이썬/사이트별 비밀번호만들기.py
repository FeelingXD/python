#Quiz) 사이트별로 비밀번호를 만들어주는 코드

#예  http://naver.com
#규칙1 : http://naver.com //부분 제외하기 ->naver.com
#규칙2 : 처음 만나는 점 (.) 이후 부분은 제외 ->naver
#규칙3 : 남은 글자중 처음 세자리 + 글자의 갯수+ 글자 내'e'의 갯수 +"!"로 구성
#예 생성된 비밀번호 => nav51!

url = "http://naver.com"

my_str = url.replace("http://","") # http :// 부분 제거 => 규칙1
my_str = my_str[:my_str.index(".")]
password = my_str[:4]+str(len(my_str)) +str(my_str.count('e'))+'!'

print(f'{url}의 비밀번호는 {password} 입니다.')

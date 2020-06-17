def open_account():
    print("새로운 계좌 생성")
def deposit(balance,money):
    print("입금이 완료되엇습니다. 잔액 : {} 원 ".format(balance+money))
    return balance+money

def withdraw(balance,money):
    if balance > money :
        print("출금 완료되엇습니다.{}".format(balance-money))
        return balance-money
    else :
        print('액수가 부족합니다. X( 잔액은 {} 원 입니다.'.format(balance))
        return balance
def withdraw_night(balance,money):
    commission= 100
    return commission , balance-money-commission

balance = 0
balance = deposit(balance,1000)
balance = withdraw(balance,2000)
commission, balance=withdraw_night(balance,500)
print('수수료는 {} 원이며, 잔액은 {}원입니다.'.format(commission,balance))

#def profile(name,age,main_lang):
#        print("이름 :{}\t 나이 : {}\t 주 언어 : {}"\
#        .format(name,age,main_lang))

def profile(name,age,*language):
    print('이름 : {}\t 나이 : {}\t'.format(name,age), end =" ")

    for i in language:
        print(i,end=' ')
    print()

profile('유재석',20,'파이선','a','c','c++')
profile('김태호',20,'자바')

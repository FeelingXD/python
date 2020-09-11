from random import *

words =['apple','banana','orange']
word = choice(words)
print('answer : '+word)
letters = "app"

while True:
    succeed = True
    print()
    for w in word:
        if w in letters:
            print(w,end=' ')
        else:
            print("_" ,end=' ')
            succeed=False
    print()

    letter = input("input letter > " )# 사용자 입력받기
    if letter not in letters:
        letters += letter

    if letter in word:
        print("Correct")

    else:
        print("Wrong")
    if succeed==True:
        break

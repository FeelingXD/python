from random import *
words = ["apple",'banana','orange']
word = choice(words)
print('answer : ' + word )
letters = ''# 모든 알파뱃

while True:
    succeed = True
    print()
    for w in word: #a p p l e
        if w in letters:
            print(w, end =" ")
        else:
            print('_', end =" ")
    print()
    if succeed:
        print("sueccess")
        break

    letter = input("input letter >")
    if letter not in letters :
        letters+=letter
        if letter in word:
            print('correct')
        else:
            print('incorrect')
    break

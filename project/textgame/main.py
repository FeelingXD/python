def answerCheck(message):
    answer=input(message).lower().strip()
    return answer
if answerCheck('what you like to play? (yes/no)') =='yes':
    print('ok')
else :
    print('ok done.')

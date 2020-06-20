gun = 10

def checkpoint(soldiers):
    global gun
    gun = gun -soldiers
    print('남은 총기수 {}'.format(gun))

print('총기수 {}'.format(gun))
checkpoint(2)

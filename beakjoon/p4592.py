# not solved.
while True:
    inputs= list(map(str,input().split()))
    unique=[]
    case = int(inputs[0])
    if inputs[0]=='0':
        break
    for i in range(1,case):
        if inputs[i] not in unique:
            unique.append(inputs[i])
    unique.append('$')
    print(' '.join(unique))

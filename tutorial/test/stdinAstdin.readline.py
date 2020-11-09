import sys

length=int(sys.stdin.readline())

for i in range(length):
    if i%3==0:
        print("A")
    elif i%3==1:
        print("B")
    else:
        print("C")

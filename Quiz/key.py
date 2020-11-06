import threading

def fthread():
    global x
    x= 4
def sthread():
    print("second!")

f= threading.Thread(target=fthread)
s= threading.Thread(target=sthread)
def main():
    s.start()
    f.start()
    print(x)
main()

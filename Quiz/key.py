import threading
def fthread():

    print("first!")

def sthread():
    print("second!")

f= threading.Thread(target=fthread)
s= threading.Thread(target=sthread)

s.start()
f.start()

class test :
    def __init__(self):
        self._objectlist=[]
    @property
    def objectlist(self):
        return self._objectlist
    @objectlist.setter
    def objectlist(self,inputstr):
        self._objectlist=list(map(str,inputstr.split()))

a=test()
a.objectlist ="life is short you need python"
print(a.objectlist)

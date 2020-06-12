#structure type queue :D
class queue():
    def __init__(self):
        self.items=[]
    def seek(self):
        self.items[0]
    def Dequeue(self):
        if len(self.items)==0:
            return -1
        return self.items.pop(0)
    def Enqueue(self,item):
        self.items.append(item)
        pass
    def Print_queue(self):
        print(self.items)

q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Print_queue()
q.Dequeue()
q.Print_queue()

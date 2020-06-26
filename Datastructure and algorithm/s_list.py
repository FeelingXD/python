# list node structure
class Slist:
    class Node:
        def __init__(self,item,link):
            self.item=item
            self.next=link
    def __init__(self):
        self.head=None
        self.size=0
    def size(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def insert_front(self,item):
        if self.is_empty():
            self.head=self.Node(item,None)
        else:
            self.head=self.Node(item,self.head)
        self.size +=1
    def insert_after(self,item,p):
        p.next=Slist.Node(item,p.next)

    def delete_first(self):
        if self.is_empty():
            return -1
        else:
            self.head=self.head.next
    def search(self,p):
            if self.is_empty():
                return -1
            for k in range(self.size):
                if target==p.item:
                    return k
                p=p.next
            return None
    def print_list(self):
        p=self.head
        while p:
            if p.next!=None:
                print(p.item, '- >' , end= '')
            else:
                print(p.item)
            p=p.next
nodelist =Slist()
nodelist.__init__()
print(nodelist.is_empty())
nodelist.insert_front(5)
nodelist.insert_front(4)
nodelist.insert_front(3)
nodelist.insert_front(2)

nodelist.print_list()

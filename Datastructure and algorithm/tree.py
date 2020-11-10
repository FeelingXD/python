class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):  # 노드 갯수
        l = self.left.size() if self.left else 0  # 3항 연산
        r = self.right.size() if self.right else 0
        return l+r+1

    def depth(self):  # 깊이
        leftDepth = self.left.depth() if self.left else 0
        rightDepth = self.right.depth() if self.right else 0
        return leftDepth + 1 if leftDepth > rightDepth else rightDepth + 1


class BinaryTree:
    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0
            
    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

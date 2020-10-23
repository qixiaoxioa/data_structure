from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s"%(self.data):(self.left,self.right)},indent = 1)
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def is_empty(self):
        if self.root is None:
            return True
        return False
    def __str__(self):
        return str(self.root)

    def __insert(self,value):
        node = Node(value,None)
        if self.is_empty():
            self.root = node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = node
                    else:
                        parent_node = parent_node.left
                elif value >= parent_node.data:
                    if parent_node.right is None:
                        parent_node.right = node
                    else:
                        parent_node = parent_node.right
                node.parent = parent_node
    def insert(self,*values):
        for vaule in values:
           self.__insert(vaule)
        return self
    #前序遍历
    def preOrderStack(self,node):
        if not node:
            return None
        while node:
            print(node.data)
            self.preOrderStack(node.left)
            self.preOrderStack(node.right)
    def preOrderStack1(self,node):
        if not node:
            return None
        stack = [node]
        while len(stack) > 0:
            print(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()




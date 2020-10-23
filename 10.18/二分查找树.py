from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.data = data
        self.left =  None
        self.right = None
        self.parent = parent
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s"%(self.data):(self.left,self.right)},indent = 1)
class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root
    def __str__(self):
        return str(self.root)
    def is_empty(self):
        if self.root is None:
            return True
        return False
    # 增加
    def __insert(self,data):
        node = Node(data,parent=None)
        if self.is_empty():
            self.root = node
        else:
            parent_node = self.root
            while True:
                if data < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = node
                        break
                    else:
                        parent_node = parent_node.left
                elif data >= parent_node.data:
                    if parent_node.right is None:
                        parent_node.right = node
                        break
                    else:
                        parent_node = parent_node.right
            node.parent = parent_node
    def insert(self,*values):
        for value in values:
            self.__insert(value)
        return self
    # 查找
    def search(self,value):
        if self.is_empty():
            raise Exception("无头")
        else:
            node = self.root
            while node and node.data != value:
                if value < node.data:
                    node = node.left
                elif value >node.data:
                    node = node.right
            return node
#     移除
    def remove(self,value):
        node = self.search(value)
        while node:
            if node.left is None and node.right is None:
                self.__reassign_nodes(node,None)
            elif node.left:
                self.__reassign_nodes(node,node.left)
            elif node.right:
                self.__reassign_nodes(node,node.right)
            else:
                max_node = self.get_max()

    def __reassign_nodes(self, node, new_children):
        if new_children is not None:
            new_children.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.left = new_children
            else:
                node.parent.right = new_children
        else:
            self.root = new_children

    def get_max(self):
        pass
    def is_right(self, node):
        return node == node.parent.right






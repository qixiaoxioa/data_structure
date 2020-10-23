from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
    def __repr__(self):
        if self.left is None or self.right is None:
            return str(self.data)
        return pformat({"%s" % (self.data): (self.left, self.right)}, indent=1)
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def __str__(self):
        return str(self.root)
    def is_empty(self):
        if self.root is None:
            return True
        return False
    def __insert(self,data):
        node = Node(data,None)
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
    def insert(self,*datas):
        for data in datas:
            self.__insert(data)
            return self
    def Search(self,value):
        if self.is_empty():
            raise IndexError("无头")
        else:
            node = self.root
            while node and node.data != value:
                if value < node.data:
                    node = node.left
                if value >= node.data:
                    node = node.right
            return node
    def remove(self,value):
        node = self.Search(value)
        if node is not None:
            if node.left is None and node.right is None:
                self.__reassign_nodes(node,None)
            elif node.left:
                self.__reassign_nodes(node,node.left)
            elif node.right:
                self.__reassign_nodes(node,node.right)
            else:
                max_node = self.get_max(node.left)
                self.remove(max_node)
                node.value = max_node.value



    def __reassign_nodes(self, node,new_children):
        if new_children is not None:
            new_children.parent = node.parent
        if node.parent is not None:
            if self.is_right:
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = node
    def is_right(self,node):
        return node == node.parent.right
    def get_max(self,node = None):
        if node is None:
            node = self.root
        if not self.is_empty():
            if node.right:
                node = node.right
        return node















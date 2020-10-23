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
    def __repr__(self):
        return f"{self.root}"
    def is_empty(self):
        # if self.root is None:
        #     return True
        # return False
        return True if self.root is None else False
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
                else :
                    if data > parent_node.data:
                        if parent_node.right is None:
                            parent_node.right = node
                            break
                        else:
                            parent_node = parent_node.right
            node.parent = parent_node
    def inserts(self,*values):
        for value in values:
            self.__insert(value)
        return self
    def search(self,value):
        if self.is_empty():
            raise IndexError("无头")
        else:
            node = self.root
            while node and node.data != value:
                if value < node.data:
                    node = node.left
                elif value > node.data:
                    node = node.right
            return node
    def remove(self, item):
        node = self.search(item)
        if node is not None:
            if node.left is None and node.right is None:
                self.__reassign_nodes(node, None)
            elif node.left:
                self.__reassign_nodes(node,node.right)
            elif node.right:
                self.__reassign_nodes(node,node.right)
            else:
                node_max = self.get_max(node.left)
                self.remove(node_max)
                node.data = node_max.data


    def __reassign_nodes(self, node, new_children):
        if new_children is not None:
            new_children.parent = node.parent
        if node.parent is not None:
            if self.is_right:
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def get_max(self,node):
        if node is None:
            node = self.root
        if self.is_empty():
            while node:
                node = node.right
            return node
    def is_right(self,node):
        return node == node.parent.right

# 前序遍历
    def preOrder(self,node):
        if not node:
            return None
        print(node.value)
        print(self.preOrder(node.left))
        print(self.preOrder(node.right))
    def preOrder1(self,node):
        stack = [node]
        while len(stack) > 0:
            print(node.value,end='')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

# 中序遍历
    def midOrder(self,node):
        if not node:
            return None
        print(self.midOrder(node.left))
        print(node.value)
        print(self.midOrder(node.right))
    # 中序遍历1
    def in_oreder_stack(self,node):
        stack = []
        while node or len(stack) >0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node.data,end="")
                node = node.right
#     后序遍历
    def post_index_stack(self,node):
        





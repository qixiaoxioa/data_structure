from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.value = data
        self.left = None
        self.right = None
        self.parent = parent
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s"%(self.value):(self.left,self.right)},indent = 1)

class BinarySearchTree:
    def __init__(self,root = None):
        self.root = root
    def __str__(self):
        return str(self.root)
    def is_empty(self):
        if self.root is None:
            return True
        return False
    # 增加
    def __insert(self,value):
        node = Node(value,None)
        if self.is_empty():
            self.root = node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = node
                        break
                    else:
                        parent_node = parent_node.left
                elif value >= parent_node.value:
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
    def search(self,item):
        if self.is_empty():
            raise IndexError("无头")
        else:
            node = self.root
            while node and node.value != item:
                if item < node.value:
                    node = node.left
                elif item > node.value:
                    node = node.right
            return node
    # 移除
    def remove(self,value):
        node = self.search(value)
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

    def __reassign_nodes(self,node,new_children):
        if new_children is not None:
            new_children.parent = node.parent
        if node.parent is not None:
            if self.is_right :
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children
    # 判断是否为右孩子
    def is_right(self,node):
        return node == node.parent.right
    # 找最大值
    def get_max(self, node = None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.riught is not None:
                node = node.right
        return node
    # 前序遍历
    def preOrderTraverse(self,node):
        if not node:
            return None
        print(node.value)
        self.preOrderTraverse(node.left)
        self.preOrderTraverse(node.right)
    # 前序遍历  (非递归)
    def preOrderTraverse1(self,node):
        stack = [node]
        while len(stack) > 0:
            print(node.value,end=' ')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()
    # 中序遍历
    def in_order_stack(self,node):
        if not node:
            return None
        self.in_order_stack1(node.left)
        print(node.value)
        self.in_order_stack1(node.right)
    # 中序遍历1
    def in_order_stack1(self,node):
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node.value,end=' ')
                node = node.right
#     后序遍历
    def post_order_stack(self,node):
        if not node:
            return None
        stack1 = []
        stack2 = []
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            print(stack2.pop().value,end=' ')
#     层序遍历
    def level_Order(self,node):
        from queue import Queue
        queue = Queue()
        queue.put(node)
        while not queue.empty():
            node = queue.get() #返回队列第一个元素,并从队列中移除
            print(node.value)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)



b = BinarySearchTree()

print(b.insert(8,3,10,1,6))
print(b.search(3))

b.preOrderTraverse1(b.root)
print()
b.in_order_stack1(b.root)
print()
b.post_order_stack(b.root)


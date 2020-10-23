class Node:
    def __init__(self,data,next = None) :
        self.data = data
        self.next = None
    def __repr__(self):
        return "node({})".format(self.data)
# n = Node(1)
# print(n)
class Linklist:
    def __init__(self):
        self.head = None
    #     头部插入
    def insert_head(self,data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node
    #     尾部添加
    def append(self,data):
        if self.head :
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.insert_head(data)

    # 打印
    def __repr__(self):
        current = self.head
        string = ''
        while current is not None:
            string += "{}-->".format(current)
            current = current.next
        return  string + "END"
    # 在任意中间位置插入
    def insert(self,i,data):
        if self.head is None:
            self.insert_head(data)
        elif i == 1:
            self.insert_head(data)
        else:
            temp = self.head
            j = 1   # 步数
            pre = temp
            while j < i :
                pre = temp
                temp = temp.next
                j += 1
            new_node = Node(data)
            pre.next = new_node
            new_node.next = temp

    # 链表插入列表
    def linklist(self,object:list):
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            new_node = Node(i)
            temp.next = new_node
            temp = temp.next

#     删除头节点
    def delate_head(self):
        temp = self.head
        if self.head:
            self.head = self.head.next
        temp.next = None
        return temp
# 删除尾节点
    def delate_tail(self):
        temp = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None

#反转列表
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
#  索引,查
    def __getitem__(self, index):
        current = self.head
        if current is None:
            raise IndexError("The Linked List is empty")
        for _ in range(1,index):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next
        return current
    def get(self,index):
        return self.__getitem__(index)

# 更改
    def __setitem__(self, index:int, data):
        current = self.head
        if current is None:
            raise IndexError("The Linked List is empty")
        for _ in range(1,index):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next
        current.data = data
    def set(self,index,data):
        self.__setitem__(index,data)

ll = Linklist()
ll.insert_head(1)
ll.insert_head(3)
ll.insert_head(4)
ll.insert_head(2)
ll.append(3)
ll.insert(3,12)
ll.delate_tail()
ll.linklist(list(range(4)))
print(ll)
ll.reverse()
print(ll)
ll.get(3)
print(ll.get(3))
ll.set(3,6)
# print(ll.delate_head())
print(ll)





# # 建立节点===============================================
# class Node:
#     def __init__(self,data,next = None):
#         self.data = data
#         self.next = None
#     def __repr__(self):
#         return 'node({})'.format(self.data)
# # n = Node(1)
# # print(n)
# # 链表
# class Linklist:
#     # 初始化
#     def __init__(self):
#         self.head = None     # 先让头部指针指向空
#     # 打印
#     def __repr__(self):
#         current = self.head
#         string = ''
#         while current is not None:
#             string += '{}-->'.format(current)
#             current = current.next
#         return string + 'END'
#
#     # 头部插入
#     def insert_head(self,data):
#         new_node = Node(data)
#         if self.head :
#             new_node.next = self.head
#         self.head = new_node
# #   尾部插入
#     def append(self,data):
#         if self.head:
#             temp = self.head
#             while temp.next :
#                 temp = temp.next
#             temp.next = Node(data)
# #     在任意位置插入
#     def insert(self,i,data):
#         if self.head is None:
#             self.insert_head(data)
#         elif i == 1:
#             self.insert_head(data)
#         else:
#             temp = self.head
#             pre = temp
#             j = 1
#             while j < i:
#                 pre = temp
#                 temp = temp.next
#                 j += 1
#             new_node = Node(data)
#             pre.next = new_node
#             new_node.next = temp
# # 链表插入列表
#     def linklist(self,object:list):
#         self.head = Node(object[0])
#         temp = self.head
#         for i in object[1:]:
#             new_node = Node(i)
#             temp.next = new_node
#             temp = temp.next
# # 删除头节点
#     def delate_head(self):
#         temp = self.head
#         if self.head:
#             self.head = self.head.next
#         temp.next = None
#         return temp
# # 删除尾节点
#     def delate_tail(self):
#         temp = self.head
#         if self.head:
#             if self.head.next is None: # 如果只有头部节点
#                 self.head = None
#             else:
#                 while temp.next.next: #当下下个节点不为空
#                     temp = temp.next
#                 temp.next = None


# 建立节点==========================================================
# class Node:
#     def __init__(self,data,next = None):
#         self.data = data
#         self.next = None
#     def __repr__(self):
#         return "node({})".format(self.data)
# # 建立链表
# class SLinkList:
# #     初始化
#     def __init__(self):
#         self.head = None
# # 打印
#     def __repr__(self):
#         current = self.head
#         string = ''
#         while current :
#             string += '{}-->'.format(current)
#             current = current.next
#         return string + 'END'
#
# # 头部插入
#     def insert_head(self,data):
#         new_node = Node(data)
#         if self.head:
#             new_node.next = self.head
#         self.head = new_node
#
# # 尾部插入
#     def append(self,data):
#         if self.head :
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = Node(data)
#         else:
#             self.insert_head(data)
# # 任意位置插入
#     def insert(self,i,data):
#         if self.head is None:
#             self.insert_head(data)
#         elif i == 1:
#             self.insert_head(data)
#         else:
#             temp = self.head
#             j = 1   # 步数
#             pre = temp
#             while j < i :
#                 pre = temp
#                 temp = temp.next
#                 j += 1
#             new_node = Node(data)
#             pre.next = new_node
#             new_node.next = temp
# # 链表插入列表
#     def linklist(self,object:list):
#         temp = self.head
#         self.head = Node(object[0])
#         for i in object[1:]:
#             temp.next = Node(i)
#             temp = temp.next
#
# # 删除头节点
#     def delate_head(self):
#         temp =self.head
#         if self.head :
#             self.head = self.head.next
#             temp.next = None
#
# # 删除尾节点
#     def delate_tail(self):
#         temp = self.head
#         if self.head:
#             if self.head.next is None:
#                 self.head = None
#             else:
#                 while temp.next.next:
#                     temp = temp.next
#                 temp.next = None

# 建立节点==============================================================
# class Node:
#     def __init__(self,data,next = None):
#         self.data = data
#         self.next = None
#     def __repr__(self):
#         return f"Node({self.data})"
# # 建立链表
# class SLinklist:
#     def __init__(self):
#         self.head = None
# # 打印
#     def __repr__(self):
#         current = self.head
#         string = ""
#         while current:
#             string += f"{current}-->"
#             current = current.next
#         return string + "END"
# # 头部插入
#     def insert_head(self,data):
#         new_node = Node(data)
#         if self.head:
#             new_node.next = self.head
#         self.head = new_node
# # 尾部插入
#     def append(self,data):
#         if self.head:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = Node(data)
#         else:
#             self.insert_head(data)
#
# # 任意位置插入
#     def insert(self,i,data):
#         if self.head is None:
#            self.insert_head(data)
#         elif i == 1:
#             self.insert_head(data)
#         else:
#             temp = self.head
#             prev = temp
#             j = 1
#             while j < i:
#                 prev = temp
#                 temp = temp.next
#                 j += 1
#             new_node = Node(data)
#             prev.next = new_node
#             new_node.next = temp
#
# # 链表插入列表
#     def linklist(self,object:list):
#         self.head = Node(object[0])
#         temp = self.head
#         for i in object[1:]:
#             new_node = Node(i)
#             temp.next = new_node
#             temp = temp.next
#
# # 删除头节点
#     def delate_head(self):
#         temp = self.head
#         if self.head:
#             self.head = self.head.next
#         temp.next = None
#         return temp
#
# # 删除尾节点
#     def delate_tail(self):
#         temp = self.head
#         if self.head:
#             if self.head.next is None:
#                 self.head = None
#             else:
#                 while temp.next.next:
#                     temp = temp.next
#                 temp.next = None



# 建立节点======================================
# class Node:
#     def __init__(self,data,next = None):
#         self.data = data
#         self.next = None
#     def __repr__(self):
#         return f"Node({self.data})"
# # 建立链表
# class SLinklist:
#     def __init__(self):
#         self.head = None
# # 打印
#     def __repr__(self):
#         current = self.head
#         string = ""
#         while current:
#             string += f"{current}-->"
#             current = current.next
#         return string + "END"
#
# # 头部插入
#     def insert_head(self,data):
#         new_node = Node(data)
#         if self.head:
#             new_node.next = self.head
#         self.head = new_node
#
# # 尾部插入
#     def append(self,data):
#         new_node = Node(data)
#         if self.head:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new_node
#         else:
#             self.insert_head(data)
#
# # 任意位置插入
#     def insert(self,i,data):
#         if self.head is None:
#             self.insert_head(data)
#         elif i == 1:
#             self.insert_head(data)
#         else:
#             temp = self.head
#             pre = temp
#             j = 1
#             while i < j:
#                 pre = temp
#                 temp = temp.next
#                 j += 1
#             new_node = Node(data)
#             pre.next = new_node
#             new_node.next = temp
#
# # 链表插入列表
#     def linklist(self,object:list):
#         self.head = object[0]
#         temp = self.head
#         for i in object[1:]:
#             temp.next = Node(i)
#             temp = temp.next
#
# # 删除头节点
#     def delate_head(self):
#         temp = self.head
#         if self.head:
#             self.head = self.head.next
#         temp.next = None
#         return temp
#
# # 删除尾节点
#     def delate_tail(self):
#         temp = self.head
#         if self.head :
#             if self.head.next is None:
#                 self.head = None
#             else:
#                 while temp.next.next:
#                     temp = temp.next
#                 temp.next = None


# 建立节点======================================
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"

# 建立链表
class SLinklist:
    def __init__(self):
        self.head = None
# 打印
    def __repr__(self):
        current = self.haed
        string = ""
        while current:
            string += f"{current}-->"
            current = current.next
        return string + "END"
# 头部插入
    def insert_head(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

# 尾部插入
    def append(self,data):
        temp = self.head
        if self.head:
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.insert_head(data)


# 任意位置插入
    def insert(self,i,data):
        if self.head is None:
            self.insert_head(data)
        elif i == 1:
            self.insert_head(data)
        else:
            temp = self.head
            pre = temp
            j = 1
            while j < i:
                pre = temp
                temp = temp.next
                j += 1
            new_node = Node(data)
            pre.next = new_node
            new_node.next = temp


# 链表插入列表
    def linklist(self,object:list):
        self.head = object[0]
        temp = self.head
        for i in object[1:]:
            temp.next = Node(i)
            temp = temp.next


# 删除头节点
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
                
# 建立节点=============================================
# 建立链表
# 打印
# 头部插入
# 尾部插入
# 任意位置插入
# 链表插入列表
# 删除头节点
# 删除尾节点


# 建立节点=================================================
# 建立链表
# 打印
# 头部插入
# 尾部插入
# 任意位置插入
# 链表插入列表
# 删除头节点
# 删除尾节点

# 建立节点==========================================
# 建立链表
# 打印
# 头部插入
# 尾部插入
# 任意位置插入
# 链表插入列表
# 删除头节点
# 删除尾节点


ll = SLinklist()
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)
ll.append(12)
ll.insert(3,6)
ll.linklist(list(range(4)))
# ll.delate_head()
print(ll)

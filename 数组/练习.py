# 数组
# class Array:
#     def __init__(self,capacity):
#         self.array = [None] * capacity
#         self.size = 0
#     def insert(self,index,element):
#         if index < 0 :
#             raise IndexError('下标越界')
#         if index >= len(self.array) or self.size > len(self.array):
#             self.addcapacity()
#         for i in range(self.size - 1,index - 1,-1):
#             self.array[i + 1] = self.array[i]
#         self.array[index] = element
#         self.size += 1
#     def remove(self,index):
#         if index < 0 or index >= self.size:
#             raise IndexError('下标越界')
#         for i in range(index,self.size ):
#             self.array[i] = self.array[i + 1]
#         self.size -= 1
#     def addcapacity(self):
#         new_array = [None]* len(self.array)*2
#         for i in range(self.size):
#             new_array[i] = self.array[i]
#         self.array = new_array
# ar = Array(10)
# ar.insert(0,1)
# ar.insert(1,2)
# ar.insert(2,3)
# ar.insert(1,4)
# ar.insert(2,3)
# print(ar.array)
# ar.remove(2)
# print(ar.array)

# 环
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"
def iscircle(head:Node) -> bool:
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
def detectcirclepoint(head:Node):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node2

    print(iscircle(node1))
    print(detectcirclepoint(node1))



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"
class SLinklist:
    def __init__(self):
        self.head = None
        self.tail  =None
        self.size = 0
    def get(self,index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr
    def __repr__(self):
        current = self.head
        string = ""
        while current:
            string += f"{current}-->"
            current = current.next
        return string + "END"
    # 增
    def insert(self,index,data):
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise Exception("索引越界")
        else:
            if self.size == 0:
                self.head = new_node
                self.tail = new_node
            elif index == 0:
                new_node.next = self.head
                self.head = new_node
            elif index == self.size:
                self.tail.next = new_node
                self.tail = new_node
            else:
                prev = self.get(index - 1)
                new_node.next = prev.next
                prev.next = new_node
            self.size += 1
    #  删
    def remove(self,index):
        if index < 0 or index >= self.size:
            raise Exception("索引越界")
        if index == 0:
            remove_node = self.head
            self.head = self.head.next
            remove_node.next = None
        elif index == self.size - 1:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = prev.next.next
        self.size -= 1
        return remove_node
        # 反转列表
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev





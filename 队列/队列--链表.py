class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"{self.data}"

class Linkarray:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def is_empty(self):
        return self.head is None
    def put(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    def pop(self):
        if self.is_empty():
            raise Exception("空列")
        else:
            remove = self.head
            self.head = self.head.next
            remove.next = None
        self.size -= 1
        return remove
    def __repr__(self):
        curr = self.head
        string = ""
        while curr:
            string += f"{curr}-->"
            curr = curr.next
        return string + "END"
if __name__ == '__main__':
    l = Linkarray()
    l.put(3)
    l.put(2)
    l.put(1)
    l.put(4)
    print(l)
    l.pop()
    print(l)


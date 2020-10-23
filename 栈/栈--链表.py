class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"

class Linkstack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self,item):
        new_node = Node(item)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if self.top:
            node = self.top
            self.top = node.next
            node.next = None
            self.size -= 1
        return node.data
    def peek(self):
        return self.top
    def is_empty(self):
        return self.top is None
    def capacity(self):
        return self.size
    def __repr__(self):
        current = self.top
        string = ""
        while current:
            string += f"{current}-->"
            current = current.next
        return string + "END"

if __name__ == '__main__':
    l = Linkstack()
    for i in range(10):
        l.push(i)
    print(l)
    for i in range(5):
        l.pop()
    print(l.pop())



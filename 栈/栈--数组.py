class Stack:
    def __init__(self,limit:10):
        self.stack = []
        self.size = 0
    def __str__(self):
        return str(self.stack)
    def push(self,data):
        self.stack.append(data)
        self.size += 1
    def pop(self):
        if self.stack:
            temp = self.stack.pop()
            self.size -= 1
            return temp
        else:
            raise IndexError("下标越界")
    def peek(self):   # 返回栈顶
        if self.stack:
            return self.stack[-1]
    def is_empty(self):
        return not bool(self.stack)
    def long(self):
        return self.size
if __name__ == '__main__':
    s = Stack(10)
    for i in range(10):
        s.push(i)
    print(s)
    for i in range(5):
        s.pop()
    print(s)
    print(s.peek())
    print(s.is_empty())
    print(s.long())



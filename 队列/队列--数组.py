class Arrayqueue:
    def __init__(self):
        self.entries = []
        self.size = 0
    def __repr__(self):
        return "<"+str(self.entries)[1:-1]+">"
    def enqueue(self,data):
        self.entries.append(data)
        self.size += 1
    def dequeue(self):
        temp = self.entries[0]
        self.entries = self.entries[1:]
        self.size -=1
        return temp
    def get(self,index):
        curr = self.entries[index]
        return curr
    def capacity(self):
        return self.size

a = Arrayqueue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)
print(a)
a.dequeue()
print(a)
print(a.get(3))
print(a.capacity())





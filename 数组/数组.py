class array:
    def __init__(self, capacity):
        self.array = [None]*capacity  # 初始化capacity 个 空值(None)  数组的容量
        self.size = 0     #  有多少个数
    #  增
    def insert(self, index, element):
        if index < 0:
            raise IndexError("下标越界")
        if index >= len(self.array) or self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size - 1,index-1,-1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1
    #  删
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("下标越界")
        for i in range(index,self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1
    # 创建新数组
    def addcapacity(self):
       new_array = [None]*len(self.array)*2
       for i in range(self.size):
           new_array[i] = self.array[i]
       self.array = new_array

ar = array(10)
ar.insert(0,1)
ar.insert(1,2)
ar.insert(2,3)
ar.insert(1,4)
ar.insert(2,3)
print(ar.array)
ar.remove(2)
print(ar.array)






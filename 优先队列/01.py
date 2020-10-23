class PriorityQueue:
    def __init__(self):
        self.array = []
        self.size = 0
    def equeue(self,data):
        self.array.append(data)
        self.size += 1
        self.heapify_up()
    # 队列
    def dequeue(self):
        if self.size <= 0:
            raise IndexError("空队列")
        else:
            remove_node = self.array[0]
            self.array[0]= self.array[-1]
            del self.array[-1]
            self.heapify_down()
            return remove_node

    def heapify_up(self):
        child_index = self.size - 1
        parent_index = (child_index - 1) >> 1
        temp = self.array[child_index]
        while child_index > 0 and temp > self.array[parent_index]:
            self.array[child_index] = self.array[parent_index]
            child_index = parent_index
            parent_index = (child_index - 1) >>1
        self.array[child_index] = temp
    def heapify_down(self):
        total_index = self.size - 1
        index = 0
        while True:
            max_index = index
            if 2 * index + 1 < total_index and self.array[2 * index + 1] < self.array[max_index]:
                max_index = 2*index+1
            if 2 * index + 2 <total_index and self.array[2 * index + 2] > self.array[max_index]:
                max_index = 2 * index + 2
            if max_index == index:
                break
            self.array[index],self.array[max_index] = self.array[max_index],self.array[index]
            index = max_index


if __name__ == '__main__':
    pp = PriorityQueue()
    pp.equeue(4)
    pp.equeue(5)
    pp.equeue(3)
    pp.equeue(8)
    pp.equeue(2)
    pp.equeue(10)
    print(pp.array)
    print(pp.dequeue())
    print(pp.array)

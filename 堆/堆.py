class Heap:
    def __init__(self):
        self.data_list = []
    def get_parent_index(self,index):
        if index <= 0 or index > len(self.data_list):
            raise IndexError("错误")
        else:
            return (index-1)>>1
    def swap(self,index_a,index_b):
        self.data_list[index_a],self.data_list[index_b] = self.data_list[index_b],self.data_list[index_a]
    # 增
    def insert(self,value):
        self.data_list.append(value)
        index = len(self.data_list) - 1
        parent_index = self.get_parent_index(index)
        while self.data_list[index] > self.data_list[parent_index] and parent_index >= 0:
            self.swap(index,parent_index)
            index = parent_index
            parent_index = self.get_parent_index(index)
    #  删
    def remove(self):
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[0]
        self.heapify(0)
        return remove_data

    def heapify(self, index):
        max_index = index
        data_length = len(self.data_list) - 1
        while True:
            if 2*index + 1 <= data_length and self.data_list[2*index + 1]>self.data_list[max_index]:
                max_index = 2*index + 1
            if 2*index + 2 <= data_length and self.data_list[2*index + 2] >self.data_list[max_index]:
                max_index = 2* index + 2
            if max_index == index:
                break
            self.swap(index,max_index)
            index = max_index




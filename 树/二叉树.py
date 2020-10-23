class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def __repr__(self):
        return f"Node({self.data})"

class Tree:
    def __init__(self):
        self.root = None
    # 增加结点
    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            temp = [self.root]
            while True:
                pop_node = temp.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)
    # 找父节点
    def node_parent(self,target):
        if self.root.data == target:
            return None
        temp = [self.root]
        while temp:
            pop_node = temp.pop(0)
            if pop_node.left.data == target:
                return pop_node
            if pop_node.right.data == target:
                return pop_node
            if pop_node.left:
                temp.append(pop_node.left)
            if pop_node.right:
                temp.append(pop_node.right)
        return None

    def __repr__(self):
        curr = self.root
        string = ""
        while curr :
            string += f"{curr}" + "-->"
            curr = curr.left
        return string + "END"
t = Tree()
t.add(1)
t.add(2)
t.add(3)
t.add(4)
t.add(5)
print(t.root.left.left)
print(t.root.left.right)
print(t.node_parent(3))


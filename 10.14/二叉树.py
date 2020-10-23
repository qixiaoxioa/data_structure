class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return f"Node({self.data})"

class Tree:
    def __init__(self):
        self.root = None
    # 增
    def add(self,data):
        node = Node(self.root)
        if self.root is None:
            self.root = node
        else:
            temp = [self.root]
            while True:
                pop_node = temp.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    pop_node = pop_node.left
                    break
                elif pop_node.right is None:
                    pop_node.right = node
                    pop_node = pop_node.right
                    break
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)
#找父节点
    def node_parent(self,target):
        if self.root.data == target:
            return  None
        else:
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

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right  = None
    def __repr__(self):
        return f"Node({self.data})"
class Tree:
    def __init__(self):
        self.root = None
    def add(self,data):
        node = Node(data)
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
    def node_parent(self,target):
        if self.root is None:
            return None
        else:
            temp =[self.root]
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




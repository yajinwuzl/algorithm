# 二叉树的实现

class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root == None:
            self.root = node
        else:
            tree_list = []
            tree_list.append(self.root)
            while tree_list:
                current_node = tree_list.pop(0)
                if current_node.lchild == None:
                    current_node.lchild = node
                    return
                else:
                    tree_list.append(current_node.lchild)
                if current_node.rchild ==None:
                    current_node.rchild = node
                else:
                    tree_list.append(current_node.rchild)

    def breadth_traversal(self):
        tree_list = []
        if self.root is None:
            return
        else:
            tree_list.append(self.root)
        while tree_list:
            current_node = tree_list.pop(0)
            print(current_node)
            if current_node.lchild is not None:
                tree_list.append(current_node.lchild)
            if current_node.rchild is not None:
                tree_list.append(current_node.rchild)


    def deep_reorder_traversal(self, root):
        # tree_list = []
        if root is None:
            return
        else:
            print(root.data, end='\t')
            self.deep_reorder_traversal(root.lchild)
            self.deep_reorder_traversal(root.rchild)

    def deep_in_order_traversal(self, root):
        if root is None:
            return
        else:
            self.deep_in_order_traversal(root.lchild)
            print(root.data, end='\t')
            self.deep_in_order_traversal(root.rchild)

    def deep_post_order_traversal(self, root):
        if root is None:
            return
        else:
            self.deep_post_order_traversal(root.lchild)
            self.deep_post_order_traversal(root.rchild)
            print(root.data, end='\t')


if __name__ == '__main__':
    tree = Tree()
    # test...
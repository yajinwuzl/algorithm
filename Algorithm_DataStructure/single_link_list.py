# 链表结构

class LinkList(object):
    '''
    任何链表都有共有的方法，可以抽象出一个抽象类来管理他们
    '''
    def __init__(self, node=None):
        self.__head = node

    def add(self):
        pass

    def insert(self):
        pass

    def is_empty(self):
        pass

    def length(self):
        pass

    def travel(self):
        pass

    def append(self):
        pass

    def remove(self):
        pass

    def search(self, item):
        pass


class Node(object):
    # 一个节点包含两部分：数据和指向下一个节点的链接域
    def __init__(self, datas):
        self.datas = datas
        self.next = None

class SingleLinkList(LinkList):
    def __init__(self, node=None):
        super().__init__()
        if node != None:
            head_node = Node(node)
            self.__head = head_node
        else:
            self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        count = 0
        current_node = self.__head
        while current_node != None:
            count += 1
            current_node = current_node.next
        return count

    def travel(self):
        current_node = self.__head
        while current_node != None:
            print(current_node.datas)
            current_node = current_node.next

    def search(self, item):
        current_node = self.__head
        while current_node != None:
            if current_node.datas == item:
                return True
            current_node = current_node.next

        return False



if __name__ == '__main__':
    sll = SingleLinkList(10)
    print("result:{0}---{1}----{2}"
          .format(sll.is_empty(),
                  sll.length(),
                  sll.search(20)))


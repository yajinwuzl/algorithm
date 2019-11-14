'''
链表的实现，单向链表和双向链表都可以由一个链表抽象类抽象出来，
单向链表和双向链表的实现方法大部分都是通用的。
创建新的节点，单向链表没有前驱。
'''
class LinkList(object):
    '''
    任何链表都有共有的方法，可以抽象出一个抽象类来管理他们
    '''
    def __init__(self, node=None):
        self.__head = node

    def add(self, item):
        pass

    def insert(self, position, item):
        pass

    def is_empty(self):
        pass

    def length(self):
        pass

    def travel(self):
        pass

    def append(self, item):
        pass

    def remove(self, item):
        pass

    def search(self, item):
        pass


class Node(object):
    # 单向链表一个节点包含两部分：数据(data)和指向下一个节点的链接域(next)
    def __init__(self, datas):
        self.datas = datas
        self.next = None

class DoubleNode(object):
    # 双向链表一个新的节点包含三部分：前驱(prev)、数据(data)、后继(next)
    def __init__(self, data):
        self.data = data
        self.next = None    # 后继 指向下一个节点
        self.prev = None    # 前驱 指向前一个节点


# 单向链表
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
            print(current_node.datas, end='\t')
            current_node = current_node.next

    def search(self, item):
        current_node = self.__head
        while current_node != None:
            if current_node.datas == item:
                return True
            current_node = current_node.next

        return False

    def add(self, item):
        node = Node(item)
        node.next  = self.__head
        self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            pass
        else:
            current_node = self.__head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node

    def insert(self, position, item):
        if position <= 0:
            self.add(item)

        elif position > (self.length() - 1):
            self.append(item)

        else:
            node = Node(item)
            count = 0
            pre_node = self.__head
            while count < position-1:   # 找到position的前一个节点
                count += 1
                pre_node = pre_node.next
            node.next = pre_node.next   # 将posiotion处的next指向下一个节点的next
            pre_node.next = node    # 将position处的前一个节点的next指向插入的节点, 要保证插入新节点后，链表是连贯的，一一指向。

    def remove(self, item):
        current_node = self.__head
        pre_node = None
        while current_node != None:
            if current_node.datas == item:
                if pre_node == None:
                    self.__head = current_node.next
                else:
                    pre_node.next = current_node.next
                break   # 删除之后就跳出循环，不用再查找了
            else:
                pre_node = current_node
                current_node = current_node.next


# 双向链表
class DoubleLinkList(LinkList):
    def __init__(self, node=None):
        super().__init__()
        if node != None:
            head_node = Node(node)
            self.__head = head_node
        else:
            self.__head = node

    def add(self, item):
        node = DoubleNode(item)
        if self.is_empty():
            self.__head= node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self, item):
        node = DoubleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            current_node = self.__head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node
            node.prev = current_node

    def insert(self, position, item):
        if position <= 0:
            self.add(item)

        elif position > (self.length() - 1):
            self.append(item)

        else:
            node = DoubleNode(item)
            count = 0
            current_node = self.__head
            while count < position-1:   # 找到position的前一个节点
                count += 1
                current_node= current_node.next
            node.prev = current_node
            node.next = current_node.next
            current_node.next.prev = node
            current_node.next = node


    def travel(self):
        current_node = self.__head
        while current_node != None:
            print(current_node.data, end='\t')
            current_node = current_node.next

    def remove(self, item):
        current_node = self.__head
        while current_node != None:
            if current_node.data == item:
                if current_node == self.__head:
                    self.__head = current_node.next
                    if current_node.next:
                        current_node.next.prev = None
                else:
                    current_node.prev.next = current_node.next
                    if current_node.next:
                        current_node.next.prev = current_node.prev
                break   # 删除之后就跳出循环，不用再查找了
            else:
                current_node = current_node.next

    def is_empty(self):
        return self.__head == None

    def length(self):
        count = 0
        current_node = self.__head
        while current_node != None:
            count += 1
            current_node = current_node.next
        return count


if __name__ == '__main__':
    dssl = DoubleLinkList()
    dssl.add(32)
    dssl.append(12)
    dssl.append(1223)
    dssl.insert(2, 1123)
    dssl.insert(4, 653)
    dssl.insert(6, 4321)
    dssl.travel()
    dssl.remove(32)
    print()
    dssl.travel()
    dssl.remove(1223)
    print()
    dssl.travel()
    dssl.remove(4321)
    print()
    dssl.travel()

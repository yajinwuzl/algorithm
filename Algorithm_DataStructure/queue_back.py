# Queue

class Queue(object):
    def __init__(self):
        self.__list = []

    def enqueue(self,item):
        return self.__list.insert(0, item)

    def dequeue(self):
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)
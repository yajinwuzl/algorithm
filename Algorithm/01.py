# 冒泡排序， 对列表进行升序排序

def bubble_sort(alist):         # 相邻两个元素进行比较，如果发现位置错误则进行交换
    n = len(alist)
    for k in range(n-1):
        for i in range(n-1-k):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


alist = [7,5,4,3,54,36,1]
bubble_sort(alist)
print(alist) 
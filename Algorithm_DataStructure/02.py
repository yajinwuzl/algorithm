# 插入排序, 是稳定的。

def insert_sort(alist):
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[1]
            else:
                break
            i -= 1



if __name__ == '__main__':
    alist = [54,226,93,17,77,31,44,55,20]
    insert_sort(alist)
    print(alist)

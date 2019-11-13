# 二分查找算法，查找的数据必须是有顺序的

def binary_search(datas, value):
    n = len(datas)
    if n == 0:
        return False
    median = n // 2
    if datas[median] == value:
        return True
    elif datas[median] < value:
        return binary_search(datas[median+1:], value)
    else:
        return binary_search(datas[0:median], value)


if __name__ == '__main__':
    datas = [12,32,1,2,345,43]
    print(binary_search(datas, 34))


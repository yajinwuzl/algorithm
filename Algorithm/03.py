# 归并排序

def merge_sort(alist):
    # 分解
    n = len(alist)
    if n<=1:
        return alist
    mid = n // 2
    left_merg_sort = merge_sort(alist[:mid])
    right_merg_sort = merge_sort(alist[mid:])

    # 合并
    result = []
    print(left_merg_sort, right_merg_sort)
    left_pointer, right_pointer = 0, 0
    while left_pointer < len(left_merg_sort) and right_pointer < len(right_merg_sort):
        if left_merg_sort[left_pointer] < right_merg_sort[right_pointer]:
            result.append(left_merg_sort[left_pointer])
            left_pointer += 1

        else:
            result.append(right_merg_sort[right_pointer])
            right_pointer += 1
    print(left_pointer)
    print(left_merg_sort)
    result.extend(left_merg_sort[left_pointer])
    result.extend(right_merg_sort[right_pointer])
    return result

if __name__ == '__main__':
    alist = [12,23,43,2,4,54,65,78]
    result = merge_sort(alist)
    print(result)




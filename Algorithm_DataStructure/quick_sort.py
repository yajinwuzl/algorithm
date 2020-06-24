"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: quick_sort.py 
@time: 2020/06/08
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

import random
from typing import List

def quick_sort(a=List[int]):
    _quick_sort_between(a, 0, len(a)-1)

def _quick_sort_between(a, low, high):
    if low < high:
        k = random.randint(low, high)
        a[low], a[k] = a[k], a[low]
        m = _partition(a, low, high)
        _quick_sort_between(a, low, m - 1)
        _quick_sort_between(a, m + 1, high)

def _partition(a, low, high):
    pivot, j = a[low], low
    for i in range(low+1, high+1):
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[low], a[j] = a[j], a[low]
    return j

def sort_t():
    a = [3,5,7,9]
    quick_sort(a)
    assert a == [3,5,7,9]
    a1 = [2,2,2,2]
    quick_sort(a1)
    assert a1 == [2,2,2,2]
    a2 = [4,3,2,1]
    quick_sort(a2)
    assert a2 == [1,2,3,4]
    a3 = [3,1,6,9,-1,-5,10,2]
    quick_sort(a3)
    assert a3 == [-5,-1,1,2,3,6,9,10]
    print("done!")

if __name__ == '__main__':
    sort_t()
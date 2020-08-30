学习笔记

### Topic

位运算、布隆过滤器、LRU缓存、排序算法

### 位运算

1.知识点

    (1).位运算符：
        左移  <<  0011=>0110
        右移  >>  0110=>0011
        按位或  |  
        按位与  &
        按位取反   ~
        按位异或   ^
    (2).重要公式：
        清除 n 最低位的 1：n & (n - 1)
        获取 n 最低位的 1：n & -n
        整除 2：n >> 1
        判断奇偶： n & 1 == 1 | 0
        n & ~n = 0
        
### 布隆过滤器（Bloom Filter）

1.概念

布隆过滤器由一个很长的二进制向量和一系列随机映射函数组成。用于检索一个元素是否在一个集合中，布隆过滤器是一个快速判断元素是否存在集合的算法。

2.特点

    (1).不需要像哈希表一样存额外的信息；
    (2).只能判断肯定不存在或可能存在；
    (3).适合用作高速缓存，如判断为可能存在，再到数据库中查询；
    (4).每个元素的存在用几个二进制位置 1 来表示；

3.适用场景

多用于大型分布式系统如比特币网络、Redis缓存、垃圾邮件过滤器、评论过滤器等；

4.代码示例

    from bitarray import bitarray 
    import mmh3 
    class BloomFilter: 
        def __init__(self, size, hash_num): 
            self.size = size 
            self.hash_num = hash_num 
            self.bit_array = bitarray(size) 
            self.bit_array.setall(0) 
        def add(self, s): 
            for seed in range(self.hash_num): 
                result = mmh3.hash(s, seed) % self.size 
                self.bit_array[result] = 1 
        def lookup(self, s): 
            for seed in range(self.hash_num): 
                result = mmh3.hash(s, seed) % self.size 
                if self.bit_array[result] == 0: 
                    return "Nope" 
            return "Probably" 
    bf = BloomFilter(500000, 7) 
    bf.add("dantezhao") 
    print (bf.lookup("dantezhao")) 
    print (bf.lookup("yyj")) 


### LRU缓存(Latest Recently Used )

1.两个要素

大小、替换策略

2.实现

Hash Table + Double LinkedList

3.需求

增加删除数据的时间复杂度为O(1)
随机访问数据的时间复杂度为O(1)

4.代码示例

    class LRUCache(object): 

	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity

	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 

	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
		
###排序算法

1.排序算法执行效率分析，衡量指标

    (1).最好情况、最坏情况、平均情况时间复杂度;
    (2).时间复杂度的系数、常数 、低阶;
    (3).比较次数和交换（或移动）次数.
    
2.排序算法实现(参考：https://segmentfault.com/u/nanfengyinan)

    (1).冒泡排序
        a.概念：冒泡排序只会操作相邻的两个数据。每次冒泡操作都会对相邻的两个元素进行比较，看是否满足大小关系要求。
               如果不满足就让它俩互换。一次冒泡会让至少一个元素移动到它应该在的位置，重复 n 次，就完成了 n 个数据的排序工作。
               
        b.代码实现：
            def bubble_sort(a: List[int]):
                length = len(a)
                if length <= 1:
                    return
            
                for i in range(length):
                    made_swap = False
                    for j in range(length - i - 1):
                        if a[j] > a[j + 1]:
                            a[j], a[j + 1] = a[j + 1], a[j]
                            made_swap = True
                    if not made_swap:
                        break
                        
    (2).插入排序
        a.概念：插入算法的核心思想是取未排序区间中的元素，在已排序区间中找到合适的插入位置将其插入，
               并保证已排序区间数据一直有序。重复这个过程，直到未排序区间中元素为空，算法结束。
        
        b.代码实现
            def insertion_sort(a: List[int]):
                length = len(a)
                if length <= 1:
                    return
            
                for i in range(1, length):
                    value = a[i]
                    j = i - 1
                    while j >= 0 and a[j] > value:
                        a[j + 1] = a[j]
                        j -= 1
                    a[j + 1] = value
                    
    (3).选择排序
        a.概念：选择排序算法的实现思路有点类似插入排序，也分已排序区间和未排序区间。
               但是选择排序每次会从未排序区间中找到最小的元素，将其放到已排序区间的末尾。
               
        b.代码实现
            def selection_sort(a: List[int]):
                length = len(a)
                if length <= 1:
                    return
            
                for i in range(length):
                    min_index = i
                    min_val = a[i]
                    for j in range(i, length):
                        if a[j] < min_val:
                            min_val = a[j]
                            min_index = j
                    a[i], a[min_index] = a[min_index], a[i]
                    
    (4).归并排序
        a.核心思想：如果要排序一个数组，我们先把数组从中间分成前后两部分，然后对前后两部分分别排序，
                  再将排好序的两部分合并在一起，这样整个数组就都有序了。使用的是分治的思想。
                  
        b.代码实现
            from typing import List
            def merge_sort(a: List[int]):
                _merge_sort_between(a, 0, len(a) - 1)
            
            def _merge_sort_between(a: List[int], low: int, high: int):
                # The indices are inclusive for both low and high.
                if low < high:
                    mid = low + (high - low) // 2
                    _merge_sort_between(a, low, mid)
                    _merge_sort_between(a, mid + 1, high)
                    _merge(a, low, mid, high)
            
            def _merge(a: List[int], low: int, mid: int, high: int):
                # a[low:mid], a[mid+1, high] are sorted.
                i, j = low, mid + 1
                tmp = []
                while i <= mid and j <= high:
                    if a[i] <= a[j]:
                        tmp.append(a[i])
                        i += 1
                    else:
                        tmp.append(a[j])
                        j += 1
                start = i if i <= mid else j
                end = mid if i <= mid else high
                tmp.extend(a[start:end + 1])
                a[low:high + 1] = tmp
                
    (5).快速排序
        a.核心思想：如果要排序数组中下标从 p 到 r 之间的一组数据，我们选择 p 到 r 之间的任意一个数据作为 pivot（分区点）。
        
        b.代码实现
            import random
            def QuickSort(arr):
                # 双向排序: 提高非随机输入的性能
                # 不需要额外的空间,在待排序数组本身内部进行排序
                # 基准值通过random随机选取
                # 入参: 待排序数组, 数组开始索引 0, 数组结束索引 len(array)-1
                if arr is None or len(arr) < 1:
                    return arr
        
            def swap(arr, low, upper):
                tmp = arr[low]
                arr[low] = arr[upper]
                arr[upper] = tmp
                return arr
        
            def QuickSort_TwoWay(arr, low, upper):
                # 小数组排序i可以用插入或选择排序
                # if upper-low < 50 : return arr
                # 基线条件: low index = upper index; 也就是只有一个值的区间
                if low >= upper:
                    return arr
                # 随机选取基准值, 并将基准值替换到数组第一个元素
                swap(arr, low, int(random.uniform(low, upper)))
                temp = arr[low]
                # 缓存边界值, 从上下边界同时排序
                i, j = low, upper
                while True:
                    # 第一个元素是基准值,所以要跳过
                    i += 1
                    # 在小区间中, 进行排序
                    # 从下边界开始寻找大于基准值的索引
                    while i <= upper and arr[i] <= temp:
                        i += 1
                    # 从上边界开始寻找小于基准值的索引
                    # 因为j肯定大于i, 所以索引值肯定在小区间中
                    while arr[j] > temp:
                        j -= 1
                    # 如果小索引大于等于大索引, 说明排序完成, 退出排序
                    if i >= j:
                        break
                    swap(arr, i, j)
                # 将基准值的索引从下边界调换到索引分割点
                swap(arr, low, j)
                QuickSort_TwoWay(arr, low, j - 1)
                QuickSort_TwoWay(arr, j + 1, upper)
                return arr
        
            return QuickSort_TwoWay(arr, 0, len(arr) - 1)
            
    (6).桶排序
        a.核心思想:将要排序的数据分到几个有序的桶里，每个桶里的数据再单独进行排序。
                  桶内排完序之后，再把每个桶里的数据按照顺序依次取出，组成的序列就是有序的了。
                  
        代码实现
            from typing import List
            def bucket_sort(arr:List[int]):
                """桶排序"""
                min_num = min(arr)
                max_num = max(arr)
                # 桶的大小
                bucket_range = (max_num-min_num) / len(arr)
                # 桶数组
                count_list = [ [] for i in range(len(arr) + 1)]
                # 向桶数组填数
                for i in arr:
                    count_list[int((i-min_num)//bucket_range)].append(i)
                arr.clear()
                # 回填，这里桶内部排序直接调用了sorted
                for i in count_list:
                    for j in sorted(i):
                        arr.append(j)
                        
    (7).计数排序
        a.核心思想：将输入的数据值转化为键存储在额外开辟的数组空间中，计数排序不是基于比较的排序算法。
        b.代码实现
            from typing import List
            import itertools
            def counting_sort(a: List[int]):
                if len(a) <= 1: return
                
                # a中有counts[i]个数不大于i
                counts = [0] * (max(a) + 1)
                for num in a:
                    counts[num] += 1
                counts = list(itertools.accumulate(counts))
            
                # 临时数组，储存排序之后的结果
                a_sorted = [0] * len(a)
                for num in reversed(a):
                    index = counts[num] - 1
                    a_sorted[index] = num
                    counts[num] -= 1
                
                a[:] = a_sorted
                
    (8).基数排序
        a.核心思想：基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；
                  依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。
                  最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。
                  
        b.代码实现
            from typing import List
            def radix_sort(arr:List[int]):
                n = len(str(max(arr)))  # 记录最大值的位数
                for k in range(n):#n轮排序
                    # 每一轮生成10个列表
                    bucket_list=[[] for i in range(10)]#因为每一位数字都是0~9，故建立10个桶
                    for i in arr:
                        # 按第k位放入到桶中
                        bucket_list[i//(10**k)%10].append(i)
                    # 按当前桶的顺序重排列表
                    arr=[j for i in bucket_list for j in i]
                return arr
                
    (9).希尔排序
        a.核心思想：先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序，
        然后依次缩减增量再进行排序，待整个序列中的元素基本有序（增量足够小）时，再对全体元素进行一次直接插入排序。
        
        b.代码实现
            from typing import List
            def shell_sort(arr:List[int]):
                """
                希尔排序
                :param arr: 待排序的List
                :return: 希尔排序是就地排序(in-place)
                """
                length = len(arr)
                dist = length // 2
                
                while dist > 0:
                    for i in range(dist, length):
                        temp = arr[i]
                        j = i
                        while j >= dist and temp < arr[j-dist]:
                            arr[j] = arr[j-dist]
                            j -= dist
                        arr[j] = temp
                    dist //= 2
                    
    (10).堆排序     
        a.核心思想:将一个无序序列调整为一个堆，就能找出序列中的最大值（或最小值），
                  然后将找出的这个元素与末尾元素交换，这样有序序列元素就增加一个，无序序列元素就减少一个，
                  对新的无序序列重复操作，从而实现排序。
                  
        b.代码实现
            def build(arr:List[int], root, end):
                while True:
                    child = 2 * root + 1 # 左子节点的位置
                    if child > end: # 若左子节点超过了最后一个节点，则终止循环
                        break
                    if (child + 1 <= end) and (arr[child + 1] > arr[child]): # 若右子节点在最后一个节点之前，并且右子节点比左子节点大，则我们的孩子指针移到右子节点上
                        child += 1
                    if arr[child] > arr[root]: # 若最大的孩子节点大于根节点，则交换两者顺序，并且将根节点指针，移到这个孩子节点上
                        arr[child], arr[root] = arr[root], arr[child]
                        root = child
                    else:
                        break
            
            def heap_sort(arr:List[int]):
                n = len(arr)
                first_root = n // 2 - 1 # 确认最深最后的那个根节点的位置
                for root in range(first_root, -1, -1): # 由后向前遍历所有的根节点，建堆并进行调整
                    build(arr, root, n - 1)
                    
                for end in range(n - 1, 0, -1): # 调整完成后，将堆顶的根节点与堆内最后一个元素调换位置，此时为数组中最大的元素，然后重新调整堆，将最大的元素冒到堆顶。依次重复上述操作
                    arr[0], arr[end] = arr[end], arr[0]
                    build(arr, 0, end - 1)
                    
                    
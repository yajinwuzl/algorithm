学习笔记

### Topic

深度优先搜索(DFS)、广度优先搜索(BFS)、贪心算法、二分查找

### DFS

1.特性：

一‘撸’到底，遍历完所有节点

2.代码模版：

    # DFS一般都是借助栈实现
    
    # 递归写法
    visited = set() 

    def dfs(node, visited):
        if node in visited: # terminator
            # already visited 
            return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
			
	
	# 非递归写法, 手动维护一个栈
    def DFS(self, tree): 

	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...
	
### BFS

1.特性

地毯式层层推进，从起始顶点开始，依次往外遍历。

2.代码模板

    # BFS一般使用队列queue实现
    
    def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...

### 贪心算法

1.解题步骤

    (1).针对一组数据，我们定义了限制值和期望值，希望从中选出几个数据，在满足限制值的情况下，期望值最大;
    (2).每次选择当前情况下，在对限制值同等贡献量的情况下，对期望值贡献最大的数据;
    (3).举例测试。
    
### 二分查找

1. 概念

二分查找针对的是一个有序的数据集合，每次都通过跟区间的中间元素对比，将待查找的区间缩小为之前的一半，直到找到要查找的元素，或者区间被缩小为 0。
 
2.代码模板

    left, right = 0, len(array) - 1 
    while left <= right: 
          mid = (left + right) / 2 
          if array[mid] == target: 
                # find the target!! 
                break or return result 
          elif array[mid] < target: 
                left = mid + 1 
          else: 
                right = mid - 1
                

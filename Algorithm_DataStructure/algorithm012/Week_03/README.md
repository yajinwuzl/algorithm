学习笔记

### topic
递归、分治、回溯

### 递归
1.概念

有可重复性，通常把一个大型复杂的问题层层转化为一个与原问题相似的规模较小的问题来求解；

2.步骤

(1).有递归终止条件；
(2).处理当前逻辑；
(3).进入下一层；
(4).清理当前层；

3.代码模版

    def recursion(level, param1, param2, ...):
        # recursion terminator
        if level > MAX_LEVLE:
            process_result
            return
            
        # process logic in current level
        process(level, data...)
        
        # drill down
        self.recursion(level+1, p1, ...)
        
        # reverse the current level status if needed
        
### 分治

1.概念

求一个最近重复性问题，将其分解成一个个子问题，分而治之。

2.求解步骤

(1).建立一个递归终止条件；
(2).处理当前逻辑，将大问题如何分解成一个个子问题；
(3).下探到下一层，各个层级解决各个层级的问题；
(4).组装各个层级的结果；
(5).清理当前层。

3.代码模版

    def divide_conquer(problem, param1, param2, ...): 
      # recursion terminator 
      if problem is None: 
        print_result 
        return 
    
      # prepare data 
      data = prepare_data(problem) 
      subproblems = split_problem(problem, data) 
    
      # conquer subproblems 
      subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
      subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
      subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
      …
    
      # process and generate the final result 
      result = process_result(subresult1, subresult2, subresult3, …)
        
      # revert the current level states


### 回溯

1.概念

使用递归的方法在每一层进行尝试找出一个正确答案，最终分步没有答案，那整个问题就没有答案。

2.本质

回溯的本质在于“选择”和“撤销选择”
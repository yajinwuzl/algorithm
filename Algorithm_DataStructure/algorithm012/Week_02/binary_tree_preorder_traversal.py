"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: binary_tree_preorder_traversal.py 
@time: 2020/07/18
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
二叉树的前序遍历
实现模本：
# 根-左-右
        def pre_order(self, root):
            if root: 
                self.traverse_path.append(root.val) 
                self.pre_order(root.left) 
                self.pre_order(root.right)
'''


#递归思想
class Solution:

    def preordert_raversal(self, root):
        traverse_path = []
        if not root:
            return []

        def pre_order(root):
            if root:
                traverse_path.append(root.val)
                pre_order(root.left)
                pre_order(root.right)
        pre_order(root)
        return traverse_path


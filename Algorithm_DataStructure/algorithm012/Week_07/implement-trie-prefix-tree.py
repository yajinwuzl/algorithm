"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: implement-trie-prefix-tree.py 
@time: 2020/08/23
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""
from functools import reduce

'''
208.实现Trie(前缀树)

'''


class Trie1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = "#"


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "#" in tree:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True

class Trie2:
    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        reduce(lambda t, c: t.setdefault(c, {}), word, self.d)['end'] = None

    def search(self, word: str) -> bool:
        try:
            return 'end' in reduce(lambda t, c: t[c], word, self.d)
        except:
            return False

    def startsWith(self, prefix: str) -> bool:
        try:
            reduce(lambda t, c: t[c], prefix, self.d)
            return True
        except:
            return False
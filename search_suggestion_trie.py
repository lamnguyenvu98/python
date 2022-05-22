from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.num_words = 0
    
    def insert(self, word):
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        if not curr.end:
            curr.end = True
            curr.word = word
            self.num_words += 1
    
    def search(self, word, n_suggest_product=None):
        curr = self.root
        if n_suggest_product is None:
            n_suggest_product = self.num_words
        sub_res = []
        for char in word:
            if char not in curr.children:
                return sub_res
            curr = curr.children[char]
        
        self.suggest(curr, sub_res, n_suggest_product)
        return sub_res
        
    
    def suggest(self, node, res, n_suggest_product):
        if node.end:
            #for i in range(node.count_node):
            res.append(node.word)
            if len(res) == n_suggest_product:
                return
        
        for name in node.children:
            #print(name)
            self.suggest(node.children[name], res, n_suggest_product)
            if len(res) == n_suggest_product:
                return
            

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        res = []
        for product in sorted(products):
            trie.insert(product)
        
        for i in range(len(searchWord)):
            res.append(trie.search(searchWord[:i+1], n_suggest_product=3))
        
        return res

products = ["mobile","mouse","moneypot","monitor","mousepad", "mourinho"]
searchWord = "m"
res = Solution().suggestedProducts(products, searchWord)

print(res)
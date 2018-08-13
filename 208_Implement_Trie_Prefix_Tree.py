
# coding: utf-8

class TrieNode:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.is_end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if child == None:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.is_end = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            #node = node.children[letter]
            if node == None:
                return False
        return node.is_end
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            node = node.children.get(letter)
            if node == None:
                return False
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    obj = Trie()
    obj.insert('apple')
    print(obj.search('apple'))
    print(obj.search('app'))
    print(obj.startsWith('app'))
    obj.insert('app')
    print(obj.search('app'))
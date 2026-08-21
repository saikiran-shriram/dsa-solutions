class WordDictionaryNode :
    def __init__(self):
        self.Children = {}
        self.isEnd = False
class WordDictionary:
    def __init__(self):
        self.root = WordDictionaryNode()
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word :
            if char not in node.Children :
                node.Children[char] = WordDictionaryNode()
            node = node.Children[char]
        node.isEnd= True

    def search(self, word: str) -> bool:
       return self.dfs(self.root, 0, word)
    
    def dfs(self ,node,index,word):
        if index == len(word) :
            return node.isEnd
        char = word[index]

        if char == '.' :
            for child in node.Children.values() :
                if self.dfs(child,index+1,word):
                    return True
            return False
        else :
            if char not in node.Children :
                return False
            return self.dfs(node.Children[char],index+1,word)
            
                

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
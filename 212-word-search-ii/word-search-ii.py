class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self):
                self.Children = {}
                self.isEnd = False
                self.word = None

        root = TrieNode()

        result = []
        def fun(i , j ,node) :
            if i <0 or i >= rows or j <0 or j >= cols or board[i][j] == '#':
                return 
            char = board[i][j]
            if char not in node.Children :
                return 
            next_node = node.Children[char]
            if next_node.word:  
                result.append(next_node.word)
                next_node.word = None
            temp = board[i][j]
            board[i][j] = '#'

            fun(i + 1, j, next_node)
            fun(i - 1, j,next_node)
            fun(i, j + 1,next_node)
            fun(i, j - 1,next_node)
                
            board[i][j] = temp

        for word in words:
            node = root
            for char in word:
                if char not in node.Children:
                    node.Children[char] = TrieNode()
                node = node.Children[char]
            node.word = word

        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                fun(i, j,root)
        return result
        
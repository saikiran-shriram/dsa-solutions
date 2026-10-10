class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        current = []
        def fun(open , close):
            if len(current) ==  2*n :
                result.append(''.join(current))
                return
            if open < n :
                current.append('(')
                fun(open+1 ,close)
                current.pop()
            if close < open:
                current.append(')')
                fun(open,close+1)
                current.pop()
        fun(0,0)
        return result
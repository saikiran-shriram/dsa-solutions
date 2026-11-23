class Solution:
    def partition(self, s: str) -> list[list[str]]:
        path = []
        result = []
  
        def fun(start) :
            if start == len(s):
                result.append(path.copy())
                return
            for end in range(start, len(s)):
                current = s[start:end+1]
                if current == current[::-1]:
                    path.append(current)
                    fun(end+1)
                    path.pop()

        fun(0)
        return result
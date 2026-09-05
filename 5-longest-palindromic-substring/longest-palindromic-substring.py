class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s,left,right):
            while left>= 0 and right < len(s) and s[left]==s[right] :
                left -= 1
                right += 1
            return s[left+1:right]
        result = ''
        for i in range(len(s)) :
            odd = expand(s,i,i)
            even = expand(s,i,i+1)
            result = max(result,odd,even, key = len)
        return result
        
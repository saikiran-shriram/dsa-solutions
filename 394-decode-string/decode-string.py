class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = ""
        num = 0
        for i in range(len(s)):
            if s[i] in '0123456789':
                num = num * 10 + int(s[i])
            elif s[i] == '[':
                stack.append((num, current))
                num = 0
                current = ""
            elif s[i] == ']':
                num, previous = stack.pop()
                current = previous + num * current
                num = 0
            else:
                current += s[i]

        return current
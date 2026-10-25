class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        b1 = bin(a)[2:]
        b2 = bin(b)[2:]
        s1 = b1.count('1')
        s2 = b2.count('1')
        if s1 >= s2 :
            return int(s1*s2)
        else :
            return int(s2/s1)
        
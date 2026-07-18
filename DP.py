# Climbing Stairs - Beat 100%
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 2
        count = 0
        if n == 1 :
            return 1
        if n == 2:
            return 2
        i = 1
        while i< n-1:
            count = a + b
            a = b
            b = count
            i = i+1
        return count

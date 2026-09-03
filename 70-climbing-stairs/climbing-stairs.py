class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        count =0
        if n ==1 :
            return 1 
        if n== 2 :
            return 2
        i= 3
        while i<= n :
            count = a +b
            a = b
            b = count
            i += 1
        return count


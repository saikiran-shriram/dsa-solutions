class Solution:
    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
        p = value
        if value == 1:
            return -1
        for i in range(2, int(value**0.5) + 1):
            if value % i == 0:
                p = i
                break
        if index > 0 and value-p-2*(index-1) <= 0 :
            return -1
        rightmost = value if index == n - 1 else value + p + 2 * (n - index - 2)
        return rightmost




        
       

        
       
            
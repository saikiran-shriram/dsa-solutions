class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        count = 0
        lst =[]
        for i in range(n+1) :
            count = 0
            num = i
            while num :
                num = num & (num-1)
                count +=1 
            lst.append(count)
        return lst
        


        
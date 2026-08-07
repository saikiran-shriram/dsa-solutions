class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            a, b = a^b, (a&b) << 1
            a = a&mask
            b = b&mask
        if a <= max_int:
            return a
        else:
            return ~(a ^ mask)
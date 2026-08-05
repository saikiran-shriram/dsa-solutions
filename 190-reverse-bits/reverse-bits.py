class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:].zfill(32)
        rev_bin = binary[::-1]
        return int(rev_bin,2)

        
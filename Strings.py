# Longest Common Prefix - Beat 100%
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for i in strs[1:] :
            curr = i
            string = ""
            for j in range(len(prefix)):
                if j >= len(curr) :
                    break
                if prefix[j] == curr[j]:
                    string = string + curr[j]
                else :
                    break
            prefix = string
        return prefix


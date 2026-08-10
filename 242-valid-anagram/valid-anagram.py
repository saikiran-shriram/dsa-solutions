class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) :
            return False
        dict = {}
        for i in s :
           dict[i] = s.count(i)
        for j in t :
            if j not in dict or t.count(j) != dict[j] :
                return False
        return True
            
        
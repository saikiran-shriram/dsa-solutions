class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = {}
        dict_s2 = {}
        if len(s2) < len(s1):
            return False
        for ch in s1:
            dict_s1[ch] = dict_s1.get(ch, 0) + 1
        for ch in s2[:len(s1)]:
            dict_s2[ch] = dict_s2.get(ch, 0) + 1
        if dict_s1 == dict_s2:
            return True
        left = 0
        for right in range(len(s1)-1,len(s2)-1) :
            outgoing = s2[left]
            incoming = s2[right + 1]
            dict_s2[outgoing] -= 1
            if dict_s2[outgoing] == 0:
                del dict_s2[outgoing]
            dict_s2[incoming] = dict_s2.get(incoming,0) + 1
            if dict_s1 == dict_s2:
                return True
            left += 1
        return False
        

            
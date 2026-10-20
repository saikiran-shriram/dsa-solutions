class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        valid = 0 
        min_length = float('inf')
        window_length = 0
        dict_t = {}
        dict_s = {}
        for ch in t:
            dict_t[ch] = dict_t.get(ch, 0) + 1
        while right < len(s) :
            ch = s[right]
            dict_s[ch] = dict_s.get(ch, 0) + 1
            if ch in dict_t and dict_s[ch] == dict_t[ch]:
                valid += 1 
            while valid == len(dict_t) :
                window_length = right - left + 1
                if window_length < min_length:
                    min_length = window_length
                    start = left
                left_char = s[left]
                dict_s[left_char] -= 1
                if left_char in dict_t and dict_s[left_char] < dict_t[left_char]:
                    valid -= 1
                left += 1 
            right += 1
        if min_length == float('inf') :
            return ""
        return s[start:start + min_length]
            
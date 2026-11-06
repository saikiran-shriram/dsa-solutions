class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        left = 0
        max_freq = 0
        max_len = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            max_freq = max(max_freq,window[ch])   
            while (right - left + 1) - max_freq > k:
                left_char = s[left]
                window[left_char] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
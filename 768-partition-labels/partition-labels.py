class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        indexes = {}
        start = 0
        end = 0
        result = []
        for i, ch in enumerate(s): 
            indexes[ch] = i
        for i, ch in enumerate(s):
            end = max(end, indexes[ch])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        from collections import Counter
        freq = Counter(tasks)
        count = 0 
        max_freq = max(freq.values())
        for key in freq :
            if freq[key] == max_freq :
                count += 1
        count_max = count
        return max(len(tasks),(max_freq - 1) * (n + 1) + count_max)

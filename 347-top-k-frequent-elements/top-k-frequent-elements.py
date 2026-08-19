class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        sorted_count = sorted(count, key=count.get, reverse=True)
        for i in range(k):
            result.append(sorted_count[i])
        return result

        
        
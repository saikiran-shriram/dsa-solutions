class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        sorted_count = sorted(count, key=count.get, reverse=True)
        for i in range(k):
            result.append(sorted_count[i])
        return result

        
        
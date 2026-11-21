class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        hashmap = {0: 1}
        for num in nums:
            current_sum += num
            previous_sum = current_sum - k
            count += hashmap.get(previous_sum, 0)
            hashmap[current_sum] = hashmap.get(current_sum, 0) + 1
        return count
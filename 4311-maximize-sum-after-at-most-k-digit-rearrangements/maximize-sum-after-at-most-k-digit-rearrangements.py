class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        result = []
        for i in range(len(nums)) :
            s = str(nums[i])
            s = ''.join(sorted(s, reverse=True))
            gain = int(s) - nums[i]
            result.append(gain)
        result.sort(reverse = True)
        return sum(nums) + sum(result[:k])
        
        
        
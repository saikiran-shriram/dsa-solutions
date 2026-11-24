class Solution:
    def maxLength(self, nums: List[int]) -> int:
        import math
        max_length = 0
        for i in range(len(nums)):
            prod = 1
            gcd_val = 0
            lcm_val = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                gcd_val = math.gcd(gcd_val, nums[j])
                lcm_val = math.lcm(lcm_val, nums[j])
                if prod == gcd_val * lcm_val :
                    max_length = max(max_length,j - i + 1)
        return max_length
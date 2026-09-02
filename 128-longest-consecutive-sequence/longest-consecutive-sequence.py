class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set: 
                count = 1
                while num+1 in  num_set :
                    num +=1 
                    count += 1
                max_count = max(max_count, count)
        return max_count
                
                
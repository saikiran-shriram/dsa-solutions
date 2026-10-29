class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        result = 0
        for i in range(len(nums)):
            valid_count = 0
            freq = {}
            rank = {}
            count = 0
            for j in range(i,len(nums)) :
                if nums[j] in freq :
                    if freq[nums[j]] == rank[nums[j]]:
                        valid_count -= 1
                    freq[nums[j]] += 1
                    if freq[nums[j]] == rank[nums[j]]:
                        valid_count += 1
                else :
                    count += 1
                    rank[nums[j]] = count   
                    freq[nums[j]] = 1
                    if freq[nums[j]] == rank[nums[j]]:
                        valid_count += 1
                if valid_count == count:
                    result += 1          
        return result
                


                
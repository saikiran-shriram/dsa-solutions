class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}
        visited = []
        for i in range(len(nums)) :
            if nums[i] in visited :
                count[nums[i]] += 1
            else :
                visited.append(nums[i])
                count[nums[i]] = 1
        for i in range(k) :
            max_key = next(iter(count))
            max_val = count[max_key]
            for key in count:
                if count[key] > max_val:
                    max_val = count[key]
                    max_key = key
            result.append(max_key)
            del count[max_key]
        return result


        
        
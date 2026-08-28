class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        added = False
        if not intervals:
            result.append(newInterval)
            added = True
        for current in intervals:
            if added:
                result.append(current)
            elif current[1] < newInterval[0] :
                result.append(current)
            elif current[0] > newInterval[1] :
                result.append(newInterval)
                added = True
                result.append(current)
            else :
                newInterval[0] = min(newInterval[0],current[0])
                newInterval[1] = max(newInterval[1],current[1])
        if not added:
            result.append(newInterval)
        return result
        
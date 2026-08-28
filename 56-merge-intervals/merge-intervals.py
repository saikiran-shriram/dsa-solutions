class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if intervals == None :
            return result
        intervals.sort()
        current = intervals[0]
        for i in range(len(intervals)-1) :
                if current[1] >= intervals[i+1][0] :
                    current[1] = max(intervals[i+1][1],current[1])
                else :
                    result.append(current)
                    current = intervals[i+1]
        result.append(current)
        return result

        
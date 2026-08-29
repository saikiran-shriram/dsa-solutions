class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        current = intervals[0]
        count = 0
        for i in range(len(intervals)-1) :
            if current[1] > intervals[i+1][0] :
                if current[1] > intervals[i+1][1] :
                    current = intervals[i+1]
                count +=1
            else : 
                current = intervals[i+1]
        return count
        
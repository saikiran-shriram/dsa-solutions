class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        maxFreq = 0
        maxCount = 0
        dict = {}
        for i in range(len(tasks)) :
            if tasks[i] in dict :
                dict[tasks[i]] +=1
            else :
                dict[tasks[i]] = 1
        maxFreq = max(dict.values())
        for value in dict.values():
            if value == maxFreq:
                maxCount += 1
        result = (maxFreq - 1) * (n + 1) + maxCount
        return max(result , len(tasks))
        
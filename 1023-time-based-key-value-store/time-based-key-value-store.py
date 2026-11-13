class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append([value, timestamp])
        else:
            self.timeMap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ''
        values = self.timeMap[key]
        left = 0    
        right = len(values) - 1 
        while left <= right :   
            mid = (left + right) // 2 
            if values[mid][1] <= timestamp :
                left = mid + 1
            if values[mid][1] > timestamp :
                right = mid -1
        if right >= 0 :
            return values[right][0]
        else :
            return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
class MedianFinder:
    import heapq
    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)
        val = heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap, -val)

        if len(self.minheap) > len(self.maxheap):
            x = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -x)

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0])/2
        elif len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
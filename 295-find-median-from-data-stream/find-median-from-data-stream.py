class MedianFinder(object):

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.max_heap :
            heappush(self.max_heap,-num)
        else :
            if num > -self.max_heap[0] :
                heappush(self.min_heap,num)
            else :
                heappush(self.max_heap,-num)
        if len(self.max_heap) - len(self.min_heap) > 1 :
            x = -heappop(self.max_heap)
            heappush(self.min_heap,x)
        if len(self.min_heap) - len(self.max_heap) > 1:
            x = heappop(self.min_heap)
            heappush(self.max_heap,-x)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0])/2.0
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
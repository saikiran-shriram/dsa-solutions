class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        import heapq
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones) 
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first != second :
                val = abs(first-second)
                heapq.heappush(stones, -val)
        if stones :
            return -heapq.heappop(stones)
        else :
            return 0
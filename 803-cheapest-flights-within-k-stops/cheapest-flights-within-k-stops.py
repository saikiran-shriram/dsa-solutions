class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] *n
        dist[src] = 0
        for i in range(k+1) :
            temp = dist[:]
            for flight in flights:
                u, v, price = flight
                if dist[u] != float('inf') :
                    temp[v] = min(temp[v],dist[u]+price)
            dist = temp[:]
        if dist[dst] == float('inf') :
            return -1
        return dist[dst]
        



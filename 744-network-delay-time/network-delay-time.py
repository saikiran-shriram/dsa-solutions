class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        heap = [(0, k)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                new_dist = d + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))
        answer = max(dist[1:])
        return answer if answer != float('inf') else -1

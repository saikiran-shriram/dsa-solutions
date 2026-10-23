class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = {}
        import heapq
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]
        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
        while heap:
            time, node = heapq.heappop(heap)
            if time > dist[node]:
                continue
            for v, w in graph.get(node, []):
                new_time = time + w
                if new_time < dist[v]:
                    dist[v] = new_time
                    heapq.heappush(heap,(new_time,v))
        result = max(dist[1:])
        return result if result != float('inf') else -1
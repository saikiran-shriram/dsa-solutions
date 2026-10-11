class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        import heapq
        rows, cols = len(grid), len(grid[0])
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        result = [0] * len(queries)
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        count = 0
        for q, i in sorted_queries:
            while heap and heap[0][0] < q:
                val, r, c = heapq.heappop(heap)
                count += 1

                for nr, nc in [(r + 1, c), (r - 1, c),
                               (r, c + 1), (r, c - 1)]:
                    if (0 <= nr < rows and 0 <= nc < cols
                            and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        heapq.heappush(heap, (grid[nr][nc], nr, nc))
            result[i] = count
        return result
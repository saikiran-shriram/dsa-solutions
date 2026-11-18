class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        total_cost = 0
        edges_used = 0
        parent = list(range(n))
        def find(x) :
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
        def union(a,b) : 
            if find(a) != find(b) : 
                parent[find(b)] = find(a)
            else : 
                return False
            return True
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))
        edges.sort()
        for cost, u, v in edges :
            if union(u, v):
                total_cost += cost
                edges_used += 1
            if edges_used == n - 1:
                break
        return total_cost
        
    
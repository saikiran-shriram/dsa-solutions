class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        gap = []
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_gas < total_cost : 
            return -1
        for i,j in zip(gas,cost) :
            gap.append(i-j)
        start = 0
        tank = 0
        for i in range(len(gas)) :
            tank += gap[i]
            if tank < 0 :
                start = i+1
                tank = 0
        return start

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        ans = 0
        costs.sort(key = lambda x: (x[0] - x[1]))

        for i in range(n):
            ans += costs[i][0]
        
        for j in range(n,2*n):
            ans += costs[j][1]

           
        return ans
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        lens = len(cost)
        # 如果用bottom up會沒有考慮到如果當你走到快結尾時，犧牲一點往後奮力跳出List的操作。
        # 而不是純粹考慮當前下一個和下兩個的成本。
        dp[lens-1] = 0
        dp[lens-2] = 0
        # 如果用top down邏輯一樣只要找最後最小值
        for i in range(lens-3,-3,-1):
            # 如果 len = 10，從index 7開始
            dp[i] = min(dp[i+1]+cost[i+1], dp[i+2]+cost[i+2])
        
        print(dp)
        return min(dp[-1],dp[-2])
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 這題其實理論上不該是放在DP，甚至不用DP
        # 因為玩股票都知道，只要明天漲，就買入今天的股票
        # 只要明天跌，就不要買。把每一段的漲幅都吃下來才是最優解
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                # 👉 把漲幅加入 profit
                profit += prices[i] - prices[i-1]
        
        return profit
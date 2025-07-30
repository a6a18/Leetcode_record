class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 此題的最優解，壓縮後連DP陣列都不需要存
        lens = len(prices)
        # dp = [0] * lens

        minprice = float('inf')
        maxprofile = 0

        if lens == 1:
            return 0
        if lens == 2:
            return 0 if prices[0] > prices[1] else prices[1] - prices[0]

        for i in range(lens):
            maxprofile = max(prices[i] - minprice, maxprofile)
            minprice = min(prices[i], minprice)

        return maxprofile
            

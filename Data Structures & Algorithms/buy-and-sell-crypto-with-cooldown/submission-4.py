class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(index: int, buying: bool) -> int:
            if index >= len(prices):
                return 0
            if (index, buying) in dp:
                return dp[(index, buying)]
            
            cooldown = dfs(index + 1, buying)
            if buying:
                buy = dfs(index + 1, False) - prices[index]
                dp[(index, buying)] = max(buy, cooldown)
            else:
                sell = dfs(index + 2, True) + prices[index]
                dp[(index, buying)] = max(sell, cooldown)
            return dp[(index, buying)]
        
        return dfs(0, True)

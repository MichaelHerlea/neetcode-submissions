class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(remaining_target):
            if remaining_target < 0:
                return float("inf")
            if remaining_target == 0:
                return 0
            if remaining_target not in memo:
                best = float("inf")
                for coin in coins:
                    best = min(best, dfs(remaining_target - coin) + 1)
                memo[remaining_target] = best
            return memo[remaining_target]
        
        output = dfs(amount)
        if output == float("inf"):
            output = -1
        return int(output)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {} # key: (index, local_amount), # number of valid branches

        def dfs(index: int, local_amount: int) -> int:
            if index >= len(coins) or local_amount > amount:
                return 0
            if local_amount == amount:
                return 1
            if (index, local_amount) not in cache:
                take = dfs(index, local_amount + coins[index])
                leave = dfs(index + 1, local_amount)
                cache[(index, local_amount)] = take + leave
            return cache[(index, local_amount)]
        
        return dfs(0, 0)
            

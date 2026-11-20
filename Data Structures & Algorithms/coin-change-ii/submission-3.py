class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {} # key: (index, local_amount), # number of valid branches

        def dfs(index: int, local_amount: int) -> int:
            if (index, local_amount) not in cache:
                if index >= len(coins) or local_amount > amount:
                    cache[(index, local_amount)] = 0
                elif local_amount == amount:
                    cache[(index, local_amount)] = 1
                else:
                    take = dfs(index, local_amount + coins[index])
                    leave = dfs(index + 1, local_amount)
                    cache[(index, local_amount)] = take + leave
            return cache[(index, local_amount)]
        
        return dfs(0, 0)
            

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}

        def dfs(new_nums: list[int]) -> int:
            if not new_nums:
                return 0
            if tuple(new_nums) not in dp:
                max_val = 0
                for index in range(len(new_nums)):
                    value = new_nums[index]
                    value *= new_nums[index - 1] if index - 1 >= 0 else 1
                    value *= new_nums[index + 1] if index + 1 < len(new_nums) else 1
                    value += dfs(new_nums[:index] + new_nums[index + 1:])
                    max_val = max(max_val, value)
                dp[tuple(new_nums)] = max_val
            return dp[tuple(new_nums)]
        
        return dfs(nums)
        
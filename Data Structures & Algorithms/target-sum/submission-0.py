class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # key: (index, current_sum)

        def backtrack(index: int, current_sum: int) -> int:
            if index == len(nums):
                return 1 if current_sum == target else 0
            if (index, current_sum) not in dp:
                dp[(index, current_sum)] = backtrack(index + 1, current_sum + nums[index]) + backtrack(index + 1, current_sum - nums[index])
            return dp[(index, current_sum)]

        return backtrack(0, 0)
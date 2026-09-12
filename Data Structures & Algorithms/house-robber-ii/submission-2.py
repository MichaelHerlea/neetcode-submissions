class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(houses):
            memo = [0] * len(houses)
            for i in range(len(houses)):
                if i == 0:
                    memo[i] = houses[i]
                elif i == 1:
                    memo[i] = max(memo[0], houses[1])
                else:
                    memo[i] = max(memo[i - 2] + houses[i], memo[i - 1])
            return memo[-1]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
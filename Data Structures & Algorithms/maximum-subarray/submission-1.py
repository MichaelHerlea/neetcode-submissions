class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum: float = float("-inf")
        local_sum: float = float("-inf")
        for i in range(len(nums)):
            value: int = nums[i]
            local_sum = max(local_sum + value, value)
            max_sum = max(max_sum, local_sum)
        
        return int(max_sum)
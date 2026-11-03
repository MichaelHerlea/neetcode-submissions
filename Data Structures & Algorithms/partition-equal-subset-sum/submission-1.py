class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False
        
        target = total_sum / 2
        def dfs(index, current_sum):
            if index == len(nums) or current_sum > target:
                return False
            if current_sum == target:
                return True
            return dfs(index + 1, current_sum + nums[index]) or dfs(index + 1, current_sum)
            
        return dfs(0, 0)
        return False
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        current_subset = []
        def dfs(index):
            if index >= len(nums):
                result.append(current_subset.copy())
                return
            
            next_index = index
            while next_index < len(nums) and nums[next_index] == nums[index]:
                next_index += 1
            
            # inclusion
            current_subset.append(nums[index])
            dfs(index + 1)
            current_subset.pop()

            # exclusion
            dfs(next_index)

        dfs(0)
        return result
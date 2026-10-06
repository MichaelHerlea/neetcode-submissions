class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            middle_point = L + (R - L) // 2
            
            if nums[middle_point] == target: return middle_point
            if nums[middle_point] > target: R = middle_point - 1
            else: L = middle_point + 1
        
        return -1
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False
        
        target = total_sum / 2
        possible_sums = {0}
        for i in range(len(nums) -1, -1, -1):
            for value in list(possible_sums):
                new_value = value + nums[i]
                if new_value == target:
                    return True
                possible_sums.add(new_value)

        return False
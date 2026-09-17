class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_sum = 1
        max_sum = 1
        abs_max = max(nums)

        for number in nums:
            if number == 0:
                min_sum = 1
                max_sum = 1
                continue
            a = min_sum * number
            b = max_sum * number
            min_sum = min(a, b, number)
            max_sum = max(a, b, number)
            abs_max = max(abs_max, max_sum)
        
        return abs_max
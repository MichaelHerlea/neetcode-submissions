class Solution:
    def trap(self, height: List[int]) -> int:
        left_index, right_index = 0, len(height) - 1
        left_max, right_max = height[0], height[-1]
        output = 0

        while left_index < right_index:
            if left_max <= right_max:
                left_index += 1
                output += max(0, min(left_max, right_max) - height[left_index])
                left_max = max(left_max, height[left_index])
            else:
                right_index -= 1
                output += max(0, min(left_max, right_max) - height[right_index])
                right_max = max(right_max, height[right_index])

        return output
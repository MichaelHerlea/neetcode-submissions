class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_size = 0
        for i, h in enumerate(heights):
            start = i                
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_size = max(max_size, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            max_size = max(max_size, h * (len(heights) - i))
        return max_size
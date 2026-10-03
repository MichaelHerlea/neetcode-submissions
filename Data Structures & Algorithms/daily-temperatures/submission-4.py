class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):
            while len(stack) >= 1 and stack[-1][1] < v:
                popped = stack.pop()
                result[popped[0]] = i - popped[0]
            stack.append((i, v))
        
        return result

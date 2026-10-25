class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        visited = []
        def dfs():
            if len(nums) == 0:
                output.append(visited.copy())
                return
            for num in nums[:]:
                visited.append(num)
                nums.remove(num)
                dfs()
                nums.append(num)
                visited.pop()

        dfs()
        return output
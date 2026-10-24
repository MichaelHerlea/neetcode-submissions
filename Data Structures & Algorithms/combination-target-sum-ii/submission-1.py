class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()

        visited_candidates = []
        def dfs(index, total):
            if total == target:
                output.append(visited_candidates.copy())
                return
            if total > target or index >= len(candidates):
                return
            
            # inclusion
            visited_candidates.append(candidates[index])
            dfs(index + 1, total + candidates[index])
            visited_candidates.pop()

            # exclusion
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            dfs(next_index, total)

        dfs(0, 0)
        return output
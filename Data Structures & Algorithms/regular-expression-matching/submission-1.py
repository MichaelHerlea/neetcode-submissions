class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(s_index: int, p_index: int) -> bool:
            if p_index == len(p):
                return s_index == len(s)
            if (s_index, p_index) in dp:
                return dp[(s_index, p_index)]

            first_match = s_index < len(s) and p[p_index] in (s[s_index], '.')

            if p_index + 1 < len(p) and p[p_index + 1] == '*':
                res = dfs(s_index, p_index + 2) or (first_match and dfs(s_index + 1, p_index))
            else:
                res = first_match and dfs(s_index + 1, p_index + 1)

            dp[(s_index, p_index)] = res
            return res

        return dfs(0, 0)
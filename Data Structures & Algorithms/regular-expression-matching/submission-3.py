class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(s_index: int, p_index: int) -> bool:
            if p_index == len(p):
                return s_index == len(s)

            if (s_index, p_index) not in dp:
                first_match = s_index < len(s) and p[p_index] in (s[s_index], '.')

                if p_index + 1 < len(p) and p[p_index + 1] == '*':
                    res = dfs(s_index, p_index + 2) or (first_match and dfs(s_index + 1, p_index))
                else:
                    res = first_match and dfs(s_index + 1, p_index + 1)
                dp[(s_index, p_index)] = res

            return dp[(s_index, p_index)]

        return dfs(0, 0)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp ={}
        def dfs(s_index: int, curr_substring: str) -> int:
            if s_index >= len(s) or curr_substring != t[:len(curr_substring)]:
                return int(curr_substring == t)
            
            if (s_index, curr_substring) not in dp:
                take = dfs(s_index + 1, curr_substring + s[s_index])
                leave = dfs(s_index + 1, curr_substring)
                dp[(s_index, curr_substring)] = take + leave

            return dp[(s_index, curr_substring)]
        
        return dfs(0, "")
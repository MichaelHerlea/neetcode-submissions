class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        def dfs(s1_index: int, s2_index: int) -> bool:
            if s1_index + s2_index == len(s3):
                return True

            if (s1_index, s2_index) in dp:
                return dp[(s1_index, s2_index)]
            
            s3_index = s1_index + s2_index
            result = False
            # Take next char from s1
            if s1_index < len(s1) and s1[s1_index] == s3[s3_index]:
                result = dfs(s1_index + 1, s2_index)

            # Take next char from s2 (only if s1 path didn't already succeed)
            if not result and s2_index < len(s2) and s2[s2_index] == s3[s3_index]:
                result = dfs(s1_index, s2_index + 1)

            dp[(s1_index, s2_index)] = result
            return result
        
        return dfs(0, 0)
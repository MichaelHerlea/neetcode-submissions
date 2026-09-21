class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text2) for _ in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 if i > 0 and j > 0 else 1
                else:
                    if i > 0 and j > 0:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    elif i > 0:
                        dp[i][j] = dp[i - 1][j]
                    elif j > 0:
                        dp[i][j] = dp[i][j - 1]
        
        return dp[-1][-1]

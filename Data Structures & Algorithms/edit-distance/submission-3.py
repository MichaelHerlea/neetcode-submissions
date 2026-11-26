class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(word1_index: int, word2_index: int) -> int:
            if word1_index >= len(word1) or word2_index >= len(word2):
                return max(len(word1) - word1_index, len(word2) - word2_index)

            if word1[word1_index] == word2[word2_index]:
                return dfs(word1_index + 1, word2_index + 1)

            if (word1_index, word2_index) not in dp:
                insert = dfs(word1_index, word2_index + 1)
                delete = dfs(word1_index + 1, word2_index)
                replace = dfs(word1_index + 1, word2_index + 1)
                dp[(word1_index, word2_index)] = min(insert, delete, replace) + 1

            return dp[(word1_index, word2_index)]
        
        return dfs(0, 0)
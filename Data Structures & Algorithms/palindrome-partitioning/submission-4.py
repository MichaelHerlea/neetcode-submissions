class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        
        def palindrome_check(word: str, l: int, r: int) -> bool:
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        currently_visited = []
        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    output.append(currently_visited.copy())
                return

            if palindrome_check(s, j, i):
                currently_visited.append(s[j : i + 1])
                dfs(i + 1, i + 1)
                currently_visited.pop()

            dfs(j, i + 1)
        
        dfs(0, 0)
        return output
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        mappings = {'2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"}

        visited_characters = []
        def dfs(index):
            if index >= len(digits):
                if visited_characters: result.append(''.join(visited_characters))
                return
            for char in mappings[digits[index]]:
                visited_characters.append(char)
                dfs(index + 1)
                visited_characters.pop()
        
        dfs(0)
        return result
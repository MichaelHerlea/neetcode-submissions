class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "":
            return 0
        
        memo = {}

        def dfs(string) -> int:
            if string in memo:
                return memo[string]
            if string == "":
                return 1
            if string[0] == "0":
                return 0
            output = dfs(string[1:])
            leading_int = int(string[0])
            if len(string) >= 2 and (leading_int == 1 or (leading_int == 2 and int(string[1]) <= 6)):
                output += dfs(string[2:])
            memo[string] = output
            return output

        return dfs(s)
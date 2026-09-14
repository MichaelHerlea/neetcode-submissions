class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0
        
        def palindromeCheck(left, right):
            nonlocal output
            while left >= 0 and right < len(s) and s[left] == s[right]:
                output += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            palindromeCheck(i, i)
            palindromeCheck(i, i + 1)

        return output
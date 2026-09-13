class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""

        if s == "":
            return ""
        
        def palindromeCheck(left, right):
            nonlocal output
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(output):
                    output = s[left:right + 1]
                left -= 1
                right += 1

        for i in range(len(s)):
            palindromeCheck(i, i)
            palindromeCheck(i, i + 1)

        return output
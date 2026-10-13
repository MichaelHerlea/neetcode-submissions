class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_dict = {}
        s2_dict = {}

        for char in s1:
            if char not in s1_dict: s1_dict[char] = 0
            s1_dict[char] += 1
        
        for i in range(len(s1)):
            char = s2[i]
            if char not in s2_dict: s2_dict[char] = 0
            s2_dict[char] += 1
        
        for i in range(len(s1), len(s2)):
            if s1_dict == s2_dict: return True
            
            char = s2[i]
            if char not in s2_dict: s2_dict[char] = 0
            s2_dict[char] = s2_dict[char] + 1

            char = s2[i - len(s1)]
            s2_dict[char] -= 1
            if s2_dict[char] == 0: del s2_dict[char]
        
        return s1_dict == s2_dict

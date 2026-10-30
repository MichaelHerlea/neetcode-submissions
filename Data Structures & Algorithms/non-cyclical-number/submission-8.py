class Solution:
    def isHappy(self, n: int) -> bool:
        visited_n = set()

        while n != 1:
            if n in visited_n:
                return False
            visited_n.add(n)

            new_n = 0
            while n > 0:
                new_n += (n % 10) ** 2
                n //= 10
            n = new_n
        
        return True
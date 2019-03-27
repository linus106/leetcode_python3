from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0): return False
        reversed = 0
        while reversed < x:
            m, n = divmod(x, 10)
            reversed = reversed * 10 + n
            if reversed == x: return True
            x = m
        return True if reversed == x else False




if __name__ == "__main__":
    strxxx = 0
    result = Solution().isPalindrome(strxxx)
    print(result)




from typing import List

class Solution:
    def intToRoman(self, s: str) -> int:
        fives = ['V','L','D','']
        ones = ['I','X','C','M']
        roman = ''
        i = 0
        while num != 0:
            num, n = divmod(num, 10)
            current = ''
            if n == 9:
                current += ones[i] + ones[i+1]
            elif n == 4:
                current += ones[i] + fives[i]
            else:
                if n >= 5:
                    n = n - 5
                    current += fives[i]
                current += ones[i] * n
            roman = current + roman
            i += 1
        return roman









if __name__ == "__main__":
    result = Solution().intToRoman(1994)
    print(result)




from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I': 1, 'X': 10, 'C': 100, 'M':1000,
                'V': 5, 'L': 50, 'D': 500}
        num = last = 0
        for i in range(len(s) - 1, -1, -1):
            current = table[s[i]]
            num += (-current if current < last else current)
            last = current
        return num










if __name__ == "__main__":
    result = Solution().romanToInt('MCMXCIV')
    print(result)




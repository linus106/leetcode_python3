from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 1
        start = end = 0
        for i in range(len(s)):
            j = 0
            while i+j < len(s) and i-j >= 0 and s[i+j] == s[i-j]:
                if (2 * j + 1 > maxLength):
                    maxLength = 2 * j + 1
                    start = i-j
                    end = i+j
                j += 1
            j = 0
            while i+j+1 < len(s) and i-j >= 0 and s[i-j] == s[i+j+1]:
                if (2 * j +2 > maxLength):
                    maxLength = 2 * j + 2
                    start = i-j
                    end = i+j+1
                j += 1
        return s[start:end+1]


    def manacher(self, s: str) -> str:
        temp = '#' + '#'.join(s) + '#'
        mx = id = 0
        max = 0
        p = [0] * len(temp)
        for i in range(len(temp)):
            p[i] = min(p[2* id - i], mx - i) if mx > i else 0
            while i + p[i] + 1 < len(temp) and i - p[i] - 1 >= 0 and temp[i + p[i] + 1] == temp[i- p[i] - 1]:
                p[i] += 1
            if p[i] + i > mx:
                id = i
                mx = p[i] + i
            if p[i] > p[max]:
                 max = i
        return s[(max - p[max])//2 : (max + p[max])//2]












if __name__ == "__main__":
    str = "babad"
    result = Solution().longestPalindrome(str)
    print(result)
    result = Solution().manacher(str)
    print(result)



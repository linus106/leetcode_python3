from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        currentMatch = bool(s) and p[0] in {s[0], '.'}
        if (len(p) >= 2 and p[1] == '*') :
            return (currentMatch and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        else :
            return currentMatch and self.isMatch(s[1:], p[1:])


    def dynamic(self, s: str, p: str) -> bool:
        cache = {}
        def dp(i, j):
            if (i, j) not in cache:
                if j == len(p):
                    ans = i == len(s)
                else:
                    currentMatch = i < len(s) and p[j] in {s[i], '.'}
                    if (j+1 < len(p) and p[j+1] == '*'):
                        ans = (currentMatch and dp(i+1, j)) or dp(i, j+2)
                    else:
                        ans = currentMatch and dp(i+1, j+1)
                cache[i, j] = ans
            return cache[i, j]
        return dp(0 ,0)









if __name__ == "__main__":
    result = Solution().dynamic("aa","a*")
    print(result)




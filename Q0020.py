from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')','{':'}','[':']'}
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack or pairs[stack.pop()] != c:
                    return False
        return not stack






if __name__ == "__main__":
    result = Solution().isValid("{[]}")
    print(result)



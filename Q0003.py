from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        shown = {}
        i = j = count = 0
        for j in range(len(s)) :
            if s[j] in shown and shown[s[j]] >= i:
                i = shown[s[j]] + 1
            else :
                count = max(count, j - i + 1)
            shown[s[j]] = j
        return count


if __name__ == "__main__":
    result = Solution().lengthOfLongestSubstring("tmmzuxm")
    print(result)



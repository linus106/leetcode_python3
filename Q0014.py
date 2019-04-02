from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''
        if not strs: return common_prefix
        for i in range(len(strs[0])):
            for another in strs[1:]:
                if i >= len(another) or another[i] != strs[0][i]:
                    return common_prefix
            common_prefix += strs[0][i]
        return common_prefix




if __name__ == "__main__":
    result = Solution().longestCommonPrefix(["aa","a"])
    print(result)




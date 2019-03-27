from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0 : return -self.reverse(-x)
        result = int(str(x)[::-1])
        return (result < 2 ** 31) * result









if __name__ == "__main__":
    strxxx = -12030
    result = Solution().reverse(strxxx)
    print(result)




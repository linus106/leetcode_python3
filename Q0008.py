from typing import List
import re

class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        str = str.strip()
        pattern = '([+-]?)(\d+)'
        matched = re.match(pattern, str)
        ret = int(matched.group()) if matched else 0
        if ret > 2147483647: ret = 2147483647
        if ret < -2147483648: ret = -2147483648
        return ret




if __name__ == "__main__":
    strxxx = '  asd+56456sdf'
    result = Solution().myAtoi(strxxx)
    print(result)




from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 : return s
        m, n = divmod(len(s), 2 * numRows - 2)
        table = {}
        for i in range(numRows):
            base = line = cut = 0
            if i == 0 :
                base = 0
                line = m
                cut = (0 if n <= i else 1)
            elif i == numRows - 1:
                base = table[i - 1]
                line = m
                cut = (0 if n <= i else 1)
            else :
                base = table[i - 1]
                line = 2 * m
                cut = 0 if n <= i else (2 if n >= 2 * numRows - i - 1 else 1)
            table[i] = base + line +cut

        result = [0] * len(s)

        for i in range(len(s)):
            m, n = divmod(i, 2 * numRows - 2)
            row = n if n < numRows else 2 * numRows - n - 2
            base = line = cut = 0
            if row == 0 :
                base = 0
                line = m
                cut = 0
            elif row == numRows - 1:
                base = table[row - 1]
                line = m
                cut = (0 if n <= row else 1)
            else :
                base = table[row - 1]
                line = 2 * m
                cut = 0 if n <= row else (2 if n >= 2 * numRows - row - 1 else 1)
            print(base + line +cut)
            result[base + line +cut] = s[i]
        return ''.join(result)


    def iterStr(self, s: str, numRows: int) -> str:
        if numRows == 1 : return s
        rows = [''] * min(numRows, len(s))
        curRow = goingDown = 0
        for c in s:
            rows[curRow] += c
            if (curRow == 0 or curRow >= numRows - 1): goingDown ^= 1
            curRow += (1 if goingDown == 1 else -1)
        return ''.join(rows)

    def iterRow(self, s: str, numRows: int) -> str:
        if numRows == 1 : return s
        result = ''
        cycle = 2 * numRows - 2
        for i in range(numRows):
            j = 0
            while j + i < len(s):
                result += s[j+i]
                if i != numRows - 1 and i != 0 and j + cycle - i < len(s):
                    result += s[j + cycle - i]
                j += cycle
        return result


if __name__ == "__main__":
    str = "PAHNAPLSIIGYIR"
    result = Solution().iterRow(str, 1)
    print(result)
    print("PAHNAPLSIIGYIR")





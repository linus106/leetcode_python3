from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        room = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                room = max(room, (j - i) * min(height[i],height[j]))
        return room

    def dynamic(self, height: List[int]) -> int:
        def dp(i, j):
            if i >= j: return 0
            return max (dp(i+1,j), dp(i,j-1),  (j - i) * min(height[i],height[j]))
        return dp(0, len(height) - 1)

    def dynamicOptimize(self, height: List[int]) -> int:
        def dp(i, j):
            if i >= j: return 0
            current = (j - i) * min(height[i],height[j])
            return max (dp(i, j-1) if height[i] >= height[j] else dp(i+1,j),  current)
        return dp(0, len(height) - 1)

    def optimize(self, height: List[int]) -> int:
        i = room = 0
        j = len(height) - 1
        while i < j:
            current = (j - i) * min(height[i], height[j])
            room = max(current, room)
            if height[i] >= height[j]: j -= 1
            else: i += 1
        return room









if __name__ == "__main__":
    result = Solution().optimize([76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191])
    print(result)




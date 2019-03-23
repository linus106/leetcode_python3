from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rest_map = {}
        for i,value in enumerate(nums):
            if value in rest_map:
                return [rest_map[value], i]
            else:
                rest_map[target - value] = i

if __name__ == "__main__":
    list = [2, 7, 11, 15]
    target = 9;

    print (Solution().twoSum(list, target))





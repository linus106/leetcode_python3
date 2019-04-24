from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i+1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                if nums[i] + nums[j] > target - nums[i] - nums[j]: break
                low, high = j + 1, length - 1
                while low < high:
                    current = nums[i] + nums[j] + nums[low] + nums[high]
                    if current < target:
                        low += 1
                    elif current > target:
                        high -= 1
                    else:
                        ret.append([nums[i], nums[j], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        low += 1
                        high -= 1
        return ret


if __name__ == "__main__":
    result = Solution().fourSum([-5,-4,-3,-2,1,3,3,5],
                                -11)
    print(result)



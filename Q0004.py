from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        half1 = len1/2
        half2 = len2/2

        nums1[half1] < nums2[half2 + 1] and nums2[half2] < nums1[half1 + 1]



if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2,4]
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(result)



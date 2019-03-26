from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m < n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, half = 0, m, (m + n + 1) // 2
        while (imin <= imax):
            i = (imin + imax) // 2
            j = half - i
            if (j < 0 or (j < n and nums1[i-1] > nums2[j])):
                imax = i - 1
            elif (j > n or (j > 0 and nums2[j-1] > nums1[i])):
                imin = i + 1
            else:
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2 == 1:
                    return float(max_left)

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                return (max_left + min_right) / 2.0




if __name__ == "__main__":
    nums1 = [1,2,3,4,5]
    nums2 = []
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(result)



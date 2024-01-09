import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_merged_list = nums1+nums2
        sorted_merged_list.sort()
        if len(sorted_merged_list) % 2 == 0:
            return (sorted_merged_list[(int(len(sorted_merged_list) / 2) -1)] + sorted_merged_list[int(len(sorted_merged_list) / 2)]) / 2
        else:
            return sorted_merged_list[int(len(sorted_merged_list) / 2)]
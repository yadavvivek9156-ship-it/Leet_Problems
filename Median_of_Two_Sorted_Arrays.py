class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        medium=0
        nums1=sorted(nums1+nums2)
        n=len(nums1)
        if n % 2 == 1:
            n=n//2
            medium = nums1[n]
            return medium
        else:
            medium = (nums1[n // 2 - 1] + nums1[n // 2]) / 2.0
            return medium
        

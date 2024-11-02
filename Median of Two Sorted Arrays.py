class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = []
        mi, ni = 0, 0

        while mi < len(nums1) and ni < len(nums2):
            if nums1[mi] < nums2[ni]:
                arr.append(nums1[mi])
                mi += 1
            else:
                arr.append(nums2[ni])
                ni += 1

        arr.extend(nums1[mi:])
        arr.extend(nums2[ni:])

        leng = len(arr)
        if leng % 2 == 0:
            return (arr[leng // 2 - 1] + arr[leng // 2]) / 2.0
        else:
            return arr[leng // 2]

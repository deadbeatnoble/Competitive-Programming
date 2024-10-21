class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return pos
            if nums[i] < target:
                pos += 1
        return pos

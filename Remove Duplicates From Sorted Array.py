class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        l = len(nums)-1
        while i < l :
            if nums[i] == nums[i+1]:
                del nums[i+1]
                l -=1
            else :
                i +=1    
        return len(nums)

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0

        for n in nums:
            if n != val:
                k+=1
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
            
                
    
        return k

        
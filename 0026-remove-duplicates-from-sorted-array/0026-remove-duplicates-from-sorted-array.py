class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        
        l = 0
        r = 1

        while l<len(nums) and r<len(nums):
            if nums[l] == nums[r]:
                nums.pop(l)
            else:
                l+=1
                r+=1
        
        return len(nums)

        
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        '''
        #using 2 ptrs:
        if len(nums) == 1:
            return False
        nums.sort()
        left,right = 0,1
        while right<len(nums):
            if nums[left] == nums[right]:
                return True
            left += 1
            right += 1
        return False
        '''

        #using counter:
        '''
        nums_count = Counter(nums)
        for k,freq in nums_count.items():
            if freq > 1:
                return True
        return False
        '''
        
        #using set:
        if len(nums) > len(set(nums)):
            return True

        return False

       
        

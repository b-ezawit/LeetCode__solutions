class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_sorted = sorted(nums)
        hmap = {}

        for i,n in enumerate(nums_sorted):
            if n not in hmap:
                hmap[n] = i
        
        return [hmap[n] for n in nums]

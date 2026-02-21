class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       
        sortNums = sorted(nums)
        numMap = {}
        for i,num in enumerate(sortNums):
            if num not in numMap:
                numMap[num] = i

        return [numMap[num] for num in nums]
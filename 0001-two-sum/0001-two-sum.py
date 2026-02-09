class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        difference_holder = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in difference_holder:
                return [difference_holder[nums[i]], i]
            difference = target - nums[i]
            difference_holder[difference] = i
        
            
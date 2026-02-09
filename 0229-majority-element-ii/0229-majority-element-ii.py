class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #brute force:
        n = len(nums)
        numsCount = Counter(nums) #{3:2 , 2:1}
        targetOccurence = math.floor(n/3)

        ans = []
        for ele,freq in numsCount.items():
            if freq > targetOccurence:
                ans.append(ele)
        
        return ans

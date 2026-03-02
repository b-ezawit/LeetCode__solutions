class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        pref_sum = 0
        for i in range(n):
            pref_sum += nums[i]
            nums[i] = pref_sum
        return nums
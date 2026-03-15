class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hmap = {0:1}
        _sum = 0
        count = 0
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum - goal in hmap:
                count +=  hmap[_sum-goal]
            hmap[_sum] = hmap.get(_sum,0) + 1
        
        return count
        
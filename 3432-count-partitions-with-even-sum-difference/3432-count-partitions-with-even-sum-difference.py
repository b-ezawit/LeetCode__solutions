class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left_sum , right_sum = 0, sum(nums)
        res = 0

        for i in range(len(nums)-1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if (left_sum - right_sum)%2 == 0:
                res += 1
        return res
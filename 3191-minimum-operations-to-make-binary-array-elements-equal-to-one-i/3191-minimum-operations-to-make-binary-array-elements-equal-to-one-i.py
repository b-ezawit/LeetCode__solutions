class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0
        for i in range(n):
            if nums[i] == 0 and i > n-3:
                return -1   
            elif nums[i] == 0 and i <= n-3:
                for j in range(i,i+3):
                    if nums[j] == 0:
                        nums[j] = 1
                    else:
                        nums[j] = 0
                ops += 1
        return ops

                

        
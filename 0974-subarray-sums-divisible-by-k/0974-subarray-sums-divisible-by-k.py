class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''
        approach:
        sum[left, right] = sum[right] - sum[left-1]

        (sum[right] - sum[left-1])%k == 0
        sum[right]%k == sum[left-1]%k

        hmap = {0:1}
        store remainder
        check if sum[right]%k in the hmap, if so,  since we found a sub-array that is divisible by k, increment the hmap[remainder]+=1 and also the ans += hmap[remainder]
        '''

        hmap = {0:1}
        _sum = 0
        count = 0
        for i in range(len(nums)):
            _sum += nums[i]
            rem = _sum % k
            if rem in hmap:
                count += hmap[rem]
            hmap[rem] = hmap.get(rem,0) + 1
        return count
        
        
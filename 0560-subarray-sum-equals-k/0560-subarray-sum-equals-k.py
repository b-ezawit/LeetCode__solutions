class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #hmap = {total_of_subarr: freq}

        #total=2
        #{0:1 , 1:1}
        hmap  = {}
        hmap[0] = 1
        count = total = 0

        for n in nums:
            total += n
            if total-k in hmap:
                count += hmap[total-k]

            hmap[total] = hmap.get(total , 0) +  1

        return count

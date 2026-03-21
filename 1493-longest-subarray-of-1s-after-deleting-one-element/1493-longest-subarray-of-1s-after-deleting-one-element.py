class Solution:
    
    def longestSubarray(self, nums: List[int]) -> int:
        left_counter, right_counter, max_len = 0, 0, 0
        
        nums.append(0) 
        for i in nums:
            if i == 1:
                right_counter += 1
            else:
                max_len = max(max_len, left_counter+right_counter)
                
                left_counter = right_counter
                right_counter = 0

        if max_len == len(nums)-1:
            max_len -= 1

        return max_len
        
        
        
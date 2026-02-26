class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum = float(0)
        for i in range(k):
            sum += nums[i]

        av = sum/k
        max_av = av

        for j in range(k, len(nums)):
          
            sum = float(sum - nums[j-k] + nums[j])
            av = sum/k
            if(av > max_av):
                max_av = av
            
            
        return max_av



        

            

            


        

        
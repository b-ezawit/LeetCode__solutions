class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x<0 else 1
        
        postv_num = abs(x)
        
        s = str(postv_num)
        
        reversed_str = s[::-1]
        
        reversed_int = int(reversed_str)
        
        result =  reversed_int * sign
         
        if result < -2**31 or result > 2**31 -1:
            return 0
        else:
            return result
    
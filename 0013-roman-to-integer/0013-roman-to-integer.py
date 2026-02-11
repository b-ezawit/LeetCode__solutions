class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        pair = {
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }
        left,right = 0,1
        result = 0
        while right < len(s):
            if s[left] + s[right] in pair:
                result += pair[s[left]+s[right]]
                left += 2
                right += 2
            else:
                result += roman[s[left]]
                left += 1
                right += 1
        
        
        if left < len(s):
            result += roman[s[left]]
        
        return result

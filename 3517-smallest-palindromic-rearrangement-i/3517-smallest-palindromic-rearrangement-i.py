class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1:
            return s
        #s = "babab" n=5
        half_len = len(s)//2 #2
        half_s = list(s[:half_len]) #s[:2] 
        half_s.sort() #half_s = "ab"
        half_s = "".join(half_s)


        mid = s[len(s)//2]

        if len(s) % 2 == 0:
            return half_s + half_s[::-1]
        else:
            return half_s + mid + half_s[::-1]

        #ababa






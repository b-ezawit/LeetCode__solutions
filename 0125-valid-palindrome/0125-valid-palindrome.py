class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_joined = "".join(c for c in s if c.isalnum())
        s_joined_lower = s_joined.lower()

        left = 0
        right = len(s_joined_lower)-1

        while left<=right:
            if s_joined_lower[left]!=s_joined_lower[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True



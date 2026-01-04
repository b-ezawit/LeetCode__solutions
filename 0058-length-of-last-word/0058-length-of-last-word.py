class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = len(s) - 1

        while(i >= 0 and s[i]== ' '):
            i -= 1

        j = i
        count = 0
        for j in range(i, -1 , -1):
            if(s[j]==' '):
                break
            if(s[j] != ' '):
                count += 1
             
        return count
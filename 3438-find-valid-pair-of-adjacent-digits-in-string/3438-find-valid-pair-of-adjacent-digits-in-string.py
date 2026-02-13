class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        sCount = Counter(s)
        for i,n in enumerate(s):
            if i == len(s)-1:
                continue
            if  s[i]!=s[i+1] and sCount[s[i]] == int(s[i]) and sCount[s[i+1]] == int(s[i+1]):
                return s[i:i+2]
        return ""
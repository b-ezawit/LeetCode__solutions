class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        #using counter:
        s_count = Counter(s)
        s_sorted = sorted(s_count.items(), key=lambda x:x[1])
        ans = ""
        for val,freq in s_sorted:
            while freq > 0:
                ans += val
                freq -= 1
        
        return ans[::-1]
        


        
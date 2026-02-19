class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hmap = {}
        for char in s:
            hmap[char] = hmap.get(char,0) + 1

        sorted_s = sorted(hmap.items(),key=lambda x : x[1])
        ans = ""
        
        for val,freq in sorted_s:
            if freq>0:
                ans += val*freq
        
        return ans[::-1]



        


        
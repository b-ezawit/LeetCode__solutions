class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #k=3 s="ab"
        left = right = maxlen = currlen = maj =0
        hmap = defaultdict(int)
        
        for right in range(len(s)):
            hmap[s[right]] += 1
            #if maj<hmap[c]:
             #   maj = hmap[c]
              #  majChar = c  
            maj = max(maj, hmap[s[right]])          
            while maj + k < right-left+1:
                hmap[s[left]] -= 1
                #if majChar == s[left]:
                #   maj -= 1
                if hmap[s[left]] <= 0:
                    del hmap[s[left]]
                #maj = max(maj,hmap[s[left]])
                left += 1
            maxlen = max(maxlen,right-left+1)
        return maxlen


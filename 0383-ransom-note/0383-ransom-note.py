class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hmap = {}

        for char in magazine:
            hmap[char] = hmap.get(char, 0) + 1
        
        for r in ransomNote:
            if r not in hmap:
                return False
            
            hmap[r]  -= 1
            if hmap[r] < 0:
                return False
        return True
    
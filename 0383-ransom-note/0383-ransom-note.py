class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomCount = Counter(ransomNote)
        magazineCount = Counter(magazine)

        for val,freq in ransomCount.items():
            if freq > magazineCount[val]:
                return False

        return True
 
        
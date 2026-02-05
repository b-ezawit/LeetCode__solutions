class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ans = 0
        for string in words:
            if all(ch in chars for ch in string) and all(string.count(c) <= chars.count(c) for c in string):
                ans += len(string)
        return ans
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            n  = len(needle)
            for i in range(len(haystack)):
                if haystack[i:i+n] == needle:
                    return i
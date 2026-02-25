class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_keys = sorted(Counter(word1).keys())
        word2_keys = sorted(Counter(word2).keys())

        word1_values = sorted(Counter(word1).values())
        word2_values = sorted(Counter(word2).values())

        if word1_keys == word2_keys and word1_values == word2_values:
            return True
        return False
       
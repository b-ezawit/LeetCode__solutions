class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        if len(s) != len(pattern):
            return False
        char_to_word = {}
        word_to_char = {}

        for char,word in zip(pattern,s):
            if char in char_to_word and char_to_word[char] != word:
                return False
            char_to_word[char] = word
        
        for char,word in zip(pattern,s):
            if word in word_to_char and word_to_char[word] != char:
                return False
            word_to_char[word] = char
        
        return True



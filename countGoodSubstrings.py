# A string is *good* if there are no repeated characters
# Given a string s, return the number of good substrings of length three in s.

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        num_strings = 0 # keep track of the number of good substrings
        for i in range(len(s)):
            if len(set(s[i:i+3])) == 3: # create a set of the substring to ensure only unique substrings of length 3 are accepted 
                num_strings += 1
        
        return num_strings

'''
Given two strings, s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word of phrase formed by rearranging the letters of a different word or phrase, typically
using all the original letters exactly once.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t): # first test would be to ensure both strings are indeed the same length
            if sorted(s) == sorted(t): # then use Python's built in sorted function to check if once sorted, the strings are indeed the same
                return True
            else:
                return False
        else:
            return False
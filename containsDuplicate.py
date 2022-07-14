'''
Given an integery array nums, return true if any value appears at least twice in the array and return
false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2 = set(nums) # create a Python set out of the nums list to automatically get rid of duplicates
        if len(nums2) != len(nums): # if the length hasn't changed it's unique, else it's not!
            return True
        else:
            return False
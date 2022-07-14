class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {} # create a dictionary to keep track of nums elements and their indexes
        for i in range(len(nums)): # loop through nums to find a remainder for target - nums[i]
            remainder = target - nums[i]
            if remainder in values: # if the remainder is in the values dictionary then return the index of it stored in the dictionary with the index for i
                return(values[remainder], i)
            else:
                values[nums[i]] = i # else, store nums[i] in the dictionary and have its value be its index
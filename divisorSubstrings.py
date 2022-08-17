# The k-beauty of an integer (num) is defined as teh substrings of num when it is read as a string must meet the following conditions:
# - it has a length of k
# - it is a divisor of num

# - Given integers num and k, return the k-beauty of num.

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nums_beauty = 0 # value to keep track of the number of k-beauty
        string = str(num) # make num a string for easier operations 
        
        for i in range(len(string)):
          # loop through string's substrings of length k and make sure they meet the following criteria: 
          # - the substring is not of 0 value
          # - the substring does indeed have a length of k
          # - the substring is a divisor of num
            if (int(string[i:i+k]) != 0) and (len(string[i:i+k]) == k) and (num % int(string[i:i+k]) == 0): 
                nums_beauty += 1 # if all three conditions met, increment the number of k-beauty
        
        return nums_beauty

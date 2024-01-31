#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Example 1:

#Input: nums = [1,2,3,1]
#Output: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create a list named unique_numbers
        unique_numbers=[]
        #for taking all values use for loop
        for num in nums:
            #if the data is not in uniique_numbers append the data
            if num in unique_numbers:
                return True
            unique_numbers.append(num)
            #else return the num
            
        return False

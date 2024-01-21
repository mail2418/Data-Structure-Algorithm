'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

'''
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

from typing import List

class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
        
    def containsDuplicate2(self, nums: List[int]) -> bool:
        hash = set()
        for num in nums:
            if num in hash:
                return True
            hash.add(num)
        return False

if __name__ == "__main":
    solution = Solution()
    if solution.containsDuplicate1([1,2,3,1]):
        print("Duplicate") 
    else:
        print("Not Duplicate")

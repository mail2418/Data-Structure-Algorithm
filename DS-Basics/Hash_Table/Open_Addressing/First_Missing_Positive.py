"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
"""

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dict = {}
        lowest = 999999999
        for i in range(len(nums)):
            dict[nums[i]] = i
            if lowest > nums[i] and nums[i] > 0: lowest = nums[i]
        for j in range(len(nums)+1):
            num = 1 + j
            if num not in dict and (num < lowest or num > lowest): return num   
        return 0

if __name__=="__main__":
    nums = [1]
    print(Solution().firstMissingPositive(nums))
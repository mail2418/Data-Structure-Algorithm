"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def generate(start,subRes):
            if subRes not in res:
                res.append(subRes[:])
            for i in range(start, len(nums)):
                subRes.append(nums[i])
                generate(i+1, subRes)
                subRes.pop()  # Backtrack
        generate(0,[])
        return res
    
if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().subsets(nums))
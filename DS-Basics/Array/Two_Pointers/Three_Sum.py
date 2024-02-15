"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
from typing import List
class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        output = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left,right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    output.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
        return output
    def threeSum2(self, nums:List[int]) -> List[List[int]]:
        if len(nums) < 3 : return []
        res = []
        nums.sort()
        for i, v in enumerate(nums):
            #check apabila duplicate
            if i > 0 and v == nums[i - 1]:
                continue
            left,right = i + 1 , len(nums) -1 
            # siapkan two pointer
            while left < right:
                result = v + nums[left] + nums[right]
                if result > 0:
                    right -= 1
                    continue
                elif result < 0 :
                    left += 1
                    continue
                res.append([v, nums[left],nums[right]])
                left += 1 # agar tidak terjadi infinite looping
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
        return res

if __name__ == "__main__":
    nums = [0,0,0,0]
    print(Solution().threeSum2(nums))
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order
'''

'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
'''

from typing import List

class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        store = []
        for i in range(len(nums)):
            pivot = nums[i]
            for j in range(i+1, len(nums)):
                if(pivot + nums[j] == target):
                    store.append(i)
                    store.append(j)
        return store
    
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        check = {}
        i = 0
        while target - nums[i] not in check:
           check[nums[i]] = i
           i = i+1
        return [check[target-nums[i]],i]
    
if __name__ == "__main__":
    print(Solution().twoSum1([2,7,11,15], 9))
    print(Solution().twoSum2([2,7,11,15], 9))
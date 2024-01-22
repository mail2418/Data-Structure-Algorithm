'''
Given an integer array nums, find the  subarray with the largest sum, and return its sum.
'''

'''
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

from math import inf
from typing import List

class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        cur_max, max_till_now = 0, -inf
        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now
    def maxSubArray2(self, nums: List[int]) -> int:
        sum=0
        max=float('-inf')
        for num in nums:
            sum+=num
            if sum>max:max=sum
            if sum<0:sum=0
        return max

if __name__ == "__main__":
    print(Solution().maxSubArray1([-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))
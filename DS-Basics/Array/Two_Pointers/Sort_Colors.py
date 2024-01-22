"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function. 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""
from typing import List
class Solution:
    # Bubble Sort O(n^2)
    def sortColors1(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] > nums[j]):
                    nums[i],nums[j] = nums[j],nums[i]
    # Merge Sort O(n log n) Space(n)
    def sortColors2(self, nums: List[int]) -> None:
        if len(nums) > 1:
            right = len(nums) // 2
            left = nums[:right]
            mid = nums[right:]

            self.sortColors2(left) 
            self.sortColors2(mid)

            i = j = k = 0

            while i < len(left) and j < len(mid):
                if left[i] < mid[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = mid[j]
                    j += 1
                k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(mid):
                nums[k] = mid[j]
                j += 1
                k += 1      

    # Heap Sort O(n log n) Space(1)
    def sortColors3(self, nums: List[int]) -> None:
        def heapify(nums, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)
            
        n = len(nums)
        for i in range(n//2, -1, -1):
            heapify(nums, n, i)
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)

if __name__ == "__main__":
    nums = [2,0,1]
    Solution().sortColors2(nums)
    print(nums)
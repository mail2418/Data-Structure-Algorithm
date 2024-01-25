"""
There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. 
You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than both of them. 
More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.
"""

from typing import List

class Solution:
    #Traverse From Right to Left + Monotonic Stack
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []
        for i in range(len(heights)-1,-1,-1):
            height = heights[i]
            visible = 0
            while stack and height > stack[-1]:
                visible += 1
                stack.pop()
            if stack:
                visible +=1
            res[i] = visible
            stack.append(height)
        return res
    
if __name__ == "__main__":
    print(Solution().canSeePersonsCount([5,1,2,3,10]))
"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

"""

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        list_num = [i for i in range(1, n + 1)]
        res = []
        def generate(start, subRes):
            if len(subRes) == k:
                res.append(subRes[:])  # Make a copy of subRes to avoid modifying it later
                return
            for i in range(start, n):
                subRes.append(list_num[i])
                generate(i + 1, subRes)
                subRes.pop()  # Backtrack
                
        generate(0, [])
        return res

if __name__ == "__main__":
    n = 4
    k = 2
    print(Solution().combine(n,k))
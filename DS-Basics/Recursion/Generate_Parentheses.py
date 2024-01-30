"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(l,r,s):
            if len(s) == n * 2 : #apabila panjang string sudah sama antara left right, left=right=n
                res.append(s)
                return
            if l < n:
                generate(l+1,r,s +"(")
            if r < l:
                generate(l,r+1,s +")")
        generate(0,0,"")
        return res
    
if __name__== "__main__":
    n = 3
    print(Solution().generateParenthesis(n))
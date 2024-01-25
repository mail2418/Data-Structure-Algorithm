"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        count = 0
        for i in range(len(s)):
            count += expand(i, i)
            count += expand(i, i + 1)
        return count
if __name__ == "__main__":
    s = "aaa"
    print(Solution().countSubstrings(s))
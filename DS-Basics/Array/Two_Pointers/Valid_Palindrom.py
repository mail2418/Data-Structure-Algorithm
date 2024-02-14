"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        punc = ['"',",",":", " ",".","@","#","_","\\", "{", "}", "'","[","]","-","?",";","!",")","(","`"]
        for punc in punc:
            s = s.replace(punc, "")
        s = s.lower().strip()
        length = len(s)
        if length %2 == 0:
            pivot = int(length/2)
        elif length % 2 == 1:
            pivot = int((length + 1)/2)
        for pivot in range(pivot):
            a = s[pivot]
            b = s[-1*(pivot+1)]
            if a == b:
                continue
            else:
                return False
        return True
    
if __name__ == "__main__":
    s = s = "A man, a plan, a canal: Panama"
    # output = 
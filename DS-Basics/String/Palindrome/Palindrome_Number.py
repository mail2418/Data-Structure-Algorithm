class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        if len(num_str) == 1 : return True
        for i in range(len(num_str)//2):
            if num_str[i] != num_str[-1 - i]:
                return False
        return True
    def isPalindrome2(self, x:int) -> bool:
        return str(x) == str(x)[::-1] 

if __name__=="__main__":
    x = 1000021
    print(Solution().isPalindrome(x))
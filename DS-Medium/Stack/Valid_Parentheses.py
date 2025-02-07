class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(":")",
            "[":"]",
            "{":"}",
        }
        stack = []
        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
            elif bracket in brackets.values():
                # apabila s kosong
                if not stack:
                    return False
                pop_bracket = stack.pop()
                if brackets[pop_bracket] != bracket:
                    return False
        return len(stack) == 0

if __name__ == "__main__":
    s = "()[]{}"
    print(Solution().isValid(s))
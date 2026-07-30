class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        options = {'}':'{',']':'[',')':'('}
        for char in s:
            if char in options:
                if stack and stack[-1] == options[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False

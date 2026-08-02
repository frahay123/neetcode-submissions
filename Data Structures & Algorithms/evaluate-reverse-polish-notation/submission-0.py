class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = 0
        for char in tokens:
            if char == '+' and stack:
               stack.append(stack.pop() + stack.pop())
            elif char == '-' and stack:
                a = stack.pop()  # second operand
                b = stack.pop()  # first operand
                stack.append(b-a)
            elif char == '*' and stack:
                stack.append(stack.pop() *stack.pop())
            elif char == '/' and stack:
                a = stack.pop()  # second operand
                b = stack.pop()  # first operand
                stack.append(int(b / a))
            else:
                stack.append(int(char))
        return stack.pop()



        
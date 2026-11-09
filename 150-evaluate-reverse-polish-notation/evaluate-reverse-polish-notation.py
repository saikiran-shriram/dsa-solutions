class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        result = 0
        for i in range(len(tokens)) :
            if tokens[i] == '+' or  tokens[i] == '-' or  tokens[i] == '*' or  tokens[i] == '/' :
                val2 = stack.pop()
                val1 = stack.pop()
                if tokens[i] == '+':
                    result = val1 + val2
                    stack.append(result)
                elif tokens[i] == '-':
                    result = val1 - val2
                    stack.append(result)
                elif tokens[i] == '*':
                    result = val1 * val2
                    stack.append(result)
                else :
                    result = int(val1 / val2)
                    stack.append(result)
            else :
                stack.append(int(tokens[i]))
        return stack[-1]
             
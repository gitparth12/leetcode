from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = set(['+', '-', '*', '/'])
        for token in tokens:
            if token in operators:
                value = 0
                b = stack.pop()
                a = stack.pop()
                match token:
                    case '+':
                        value = a + b
                    case '-':
                        value = a - b
                    case '*':
                        value = a * b
                    case '/':
                        value = int(a / b)
                stack.append(value)
            else:
                stack.append(int(token))

        return stack.pop()
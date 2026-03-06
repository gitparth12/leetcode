from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token[-1].isdigit():
                stack.append(int(token))
            else:
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


        return stack.pop()
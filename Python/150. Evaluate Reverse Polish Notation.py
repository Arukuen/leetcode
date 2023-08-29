from typing import List
from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack:deque[str] = deque()
        for s in tokens:
            if s == '+': stack.append(stack.pop() + stack.pop())
            elif s == '-':
                t = stack.pop()
                stack.append(stack.pop() - t)
            elif s == '*': stack.append(stack.pop() * stack.pop())
            elif s == '/': 
                t = stack.pop()
                stack.append(int(stack.pop() / t))
            else:
                stack.append(int(s))
        return stack

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
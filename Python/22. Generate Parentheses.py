from typing import List

# Open and close is both maximum to n
# Only can add close parenthesis if open > close
# If open and close reach the maximum, return
# Recursive
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(current, open, close):
            if open == close == n:
                res.append(current)
                return
            
            if open < n:
                backtrack(current + '(', open + 1, close)

            if open > close:
                backtrack(current + ')', open, close + 1)

        backtrack('', 0, 0)
        return res

print(Solution().generateParenthesis(3))            


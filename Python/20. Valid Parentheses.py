class Solution:
    def isValid(self, s: str) -> bool:
        hash = {')': '(', ']': '[', '}': '{'}
        stack = []
        for l in s:
            if l not in hash:
                stack.append(l)
                continue
            if not stack or hash[l] != stack[-1]:
                return False
            stack.pop()
        return not stack

print(Solution().isValid("()[]{}"))
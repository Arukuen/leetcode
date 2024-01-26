class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join([chr(ord(l) + 32 if ord(l) >= 65 and ord(l) <= 90 else ord(l)) for l in s])
    
print(Solution().toLowerCase("al&phaBET"))


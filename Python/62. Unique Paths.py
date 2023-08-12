class Solution:
    def __init__(self) -> None:
        self.memo = {}
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        elif (m, n) in self.memo:
            return self.memo[(m,n)]
        self.memo[(m,n)] = self.uniquePaths(n-1, m) + self.uniquePaths(n, m-1)
        return self.memo[(m,n)]
    
print(Solution().uniquePaths(3,3))
class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def fib(self, n: int) -> int:
        if n <=1: 
            return n
        elif n in self.memo:
            return self.memo[n]
        self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]
        
sol = Solution()
print(sol.fib(3))


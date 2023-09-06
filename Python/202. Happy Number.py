from functools import reduce

class Solution:
    def isHappy(self, n: int) -> bool:
        loop_set = set()
        res = n
        while res != 1:
            res = reduce(lambda a, b: a + b**2, [0]+[int(x) for x in str(res)])
            if res in loop_set:
                return False
            loop_set.add(res)
        return True

print(Solution().isHappy(7))
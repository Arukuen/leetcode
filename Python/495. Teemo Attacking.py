from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        damage = duration
        i = 1
        while i < len(timeSeries):
            curr = timeSeries[i] - timeSeries[i-1]
            damage += duration if curr > duration else curr
            i += 1
        return damage

print(Solution().findPoisonedDuration([1,2], 2)) 
            


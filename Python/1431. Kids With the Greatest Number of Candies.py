from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies) - extraCandies
        return [True if c >= m else False for c in candies]
    

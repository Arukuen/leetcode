from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if (i-1 < 0 or flowerbed[i-1] == 0) and (i+1 >= len(flowerbed) or flowerbed [i+1] == 0):
                    n -= 1
                    i += 1
            i += 1
            if n <= 0:
                return True
        return False
    
print(Solution().canPlaceFlowers([0,1,0,1,0,1,0,0], 1))
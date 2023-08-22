from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            hash[num] = 1 + hash.get(num, 0)
        
        return sorted(hash, key=lambda h: hash[h])[-k:]
    
print(Solution().topKFrequent([4,1,-1,2,-1,2,3], 2))
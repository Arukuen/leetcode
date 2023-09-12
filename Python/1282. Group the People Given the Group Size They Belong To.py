from typing import List
import collections

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        out = []
        hash = collections.defaultdict(lambda: [])
        for i, g in enumerate(groupSizes):
            hash[g].append(i)
            if len(hash[g]) == g:
                out.append(hash[g].copy())
                hash[g].clear()
        return out


print(Solution().groupThePeople([3,3,3,3,3,1,3]))
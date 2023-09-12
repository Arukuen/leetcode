import collections

class Solution:
    def minDeletions(self, s: str) -> int:
        hash = collections.defaultdict(lambda: 0)
        freq_set = set()
        res = 0
        for l in s:
            hash[l] += 1
    
        for f in hash.values():
            while f > 0 and f in freq_set:
                f -= 1
                res += 1
            freq_set.add(f)
        return res

print(Solution().minDeletions('bbcebab'))
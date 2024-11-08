from typing import List
from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(lambda: 0)
        for letter in ransomNote:
            counter[letter] += 1

        for letter in magazine:
            if letter in counter:
                counter[letter] -= 1

        return all([c <= 0 for c in counter.values()])
    

print(Solution().canConstruct('fihjjjjei', 'hjibagacbhadfaefdjaeaebgi'))
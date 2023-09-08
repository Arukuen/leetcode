from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[1]]
        for i in range(1, numRows):
            tri.append([1])
            for j in range(1, i):
                tri[i].append(tri[i-1][j-1] + tri[i-1][j])
            tri[i].append(1)
        return tri
    
print(Solution().generate(5))
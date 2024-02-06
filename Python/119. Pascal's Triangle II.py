class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri = [[1]]
        for i in range(1, rowIndex+1):
            tri.append([1])
            for j in range(1, i):
                tri[i].append(tri[i-1][j-1] + tri[i-1][j])
            tri[i].append(1)
        return tri[rowIndex]
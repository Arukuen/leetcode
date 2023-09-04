import collections
from typing import List 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                square_index = (i // 3) * 3 + (j // 3)
                if curr == '.':
                    continue
                if curr in row[i] or curr in col[j] or curr in square[square_index]:
                    return False
                row[i].add(curr)
                col[j].add(curr)
                square[square_index].add(curr)
        return True

print(Solution().isValidSudoku(
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
))
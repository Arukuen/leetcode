from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze)-1, len(maze[0])-1
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        queue = deque([[*entrance, 0]])

        # Mark the entrance as visited
        maze[entrance[0]][entrance[1]] = '+'

        while queue:
            i, j, level = queue.popleft()

            # Check if in the corner
            if (i == 0 or j == 0 or i == m or j == n) and [i,j] != entrance:
                return level
            
            for x, y in directions:
                x, y = x + i, y + j

                # Check if still within the maze
                if 0 <= x <= m and 0 <= y <= n and maze[x][y] == '.':
                    maze[x][y] = '+'
                    queue.append((x, y, level+1))
        return -1
            
# print(Solution().nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]))
print(Solution().nearestExit([["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]], [0,1]))
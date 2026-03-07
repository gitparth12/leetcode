from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        max_area = 0

        def bfs(i: int, j: int) -> int:  # Perform bfs and return size of island
            size = 0
            fringe = deque([(i, j)])
            while fringe:
                a, b = fringe.pop()
                for coords in directions:
                    row, col = a+coords[0], b+coords[1]
                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                        fringe.appendleft((a+coords[0], b+coords[1]))
                        grid[a+coords[0]][b+coords[1]] = 2
                size += 1
            return size
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 2  # use 2 to represent visited cells
                    max_area = max(max_area, bfs(i, j))

        return max_area

def print_grid(grid: List[List[int]]):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=' ')
        print()

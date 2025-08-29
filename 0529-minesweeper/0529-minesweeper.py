class Solution:
    adjacent = [(0, 1), (1, 1), (1, 0), (-1, 1), (0, -1), (-1, -1), (-1, 0), (1, -1)]

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        print(click)
        process_click(board, click)
        return board
    
def process_click(board: List[List[str]], click: List[int]) -> List[List[str]]:
    i, j = click
    fringe = [click]
    while fringe:
        x, y = fringe.pop()
        fringe.extend(process_square(board, (x, y)))
        if board[x][y] == 'X':
            return board

def process_square(board: List[List[int]], position: List[int]):
    current = board[position[0]][position[1]]
    if current == 'M':
        board[position[0]][position[1]] = 'X'
        return []
    elif current == 'E':
        mines = count_adjacent_mines(board, position)
        if mines > 0:
            board[position[0]][position[1]] = str(mines)
            return []
        board[position[0]][position[1]] = 'B'
    
    next = []
    adjacent_squares = [(position[0] + x, position[1] + y) for x, y in Solution.adjacent if is_valid(board, (position[0]+x, position[1]+y))]
    for x, y in adjacent_squares:
        mines = count_adjacent_mines(board, (x, y))
        if mines > 0:
            board[x][y] = str(mines)
        elif board[x][y] == 'E':
            next.append((x, y))
    return next

def is_valid(board: List[List[int]], position: List[int]):
    x, y = position
    return x < len(board) and x >= 0 and y < len(board[0]) and y >= 0
        

def count_adjacent_mines(board: List[List[int]], position: List[int]):
    adjacent_squares = [board[position[0] + x][position[1] + y] for x, y in Solution.adjacent if is_valid(board, (position[0] + x, position[1] + y))]
    return adjacent_squares.count('M')
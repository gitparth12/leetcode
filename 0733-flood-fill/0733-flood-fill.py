# class Solution:
#     def isValid(self, image: List[List[int]], x, y, origin_color, color):
#         if x < 0 or x >= len(image)\
#         or y < 0 or y >= len(image[0]):
#             return False
#         if image[x][y] != origin_color or image[x][y] == color:
#             return False
#         return True

#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         start_color = image[sr][sc]
#         queue = [(sr, sc)]
#         while len(queue) > 0:
#             current_coords = queue.pop(0)
#             image[current_coords[0]][current_coords[1]] = color
#             if self.isValid(image, current_coords[0]-1, current_coords[1], start_color, color):
#                 queue.append((current_coords[0]-1, current_coords[1]))
#             if self.isValid(image, current_coords[0]+1, current_coords[1], start_color, color):
#                 queue.append((current_coords[0]+1, current_coords[1]))
#             if self.isValid(image, current_coords[0], current_coords[1]-1, start_color, color):
#                 queue.append((current_coords[0], current_coords[1]-1))
#             if self.isValid(image, current_coords[0], current_coords[1]+1, start_color, color):
#                 queue.append((current_coords[0], current_coords[1]+1))
#         return image

class Solution:
    def __init__(self):
        self.direction = ((-1, 0), (0, -1), (1, 0), (0, 1))

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # create copy of image to track visited
        m, n = len(image), len(image[0])
        visited = [[False for j in range(n)] for i in range(m)]

        starting_color = image[sr][sc]
        self.BFS(image, sr, sc, visited, m, n, color, starting_color)

        return image
    
    def BFS(self, image, i, j, visited, m, n, color, starting_color):
        # base case(s)
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if visited[i][j] or image[i][j] != starting_color:
            return
        
        # change color
        image[i][j] = color
        visited[i][j] = True

        # recurse on neighbors
        for val in self.direction:
            self.BFS(image, i+val[0], j+val[1], visited, m, n, color, starting_color)
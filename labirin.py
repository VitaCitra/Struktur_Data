import random
import os
import time
from collections import deque

WIDTH = 21
HEIGHT = 21

# Generate maze (DFS)
def generate_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        directions = [(2,0), (-2,0), (0,2), (0,-2)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == '#':
                maze[ny][nx] = ' '
                maze[y + dy//2][x + dx//2] = ' '
                carve(nx, ny)

    maze[1][1] = ' '
    carve(1, 1)

    return maze

# BFS solver
def solve_maze(maze, start, end):
    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if maze[ny][nx] == ' ' and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)

    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = parent.get(cur)
        if cur is None:
            return []
    path.append(start)
    path.reverse()
    return path

# Print maze
def print_maze(maze, pos=None, start=None, end=None):
    maze_copy = [row[:] for row in maze]

    if start:
        sx, sy = start
        maze_copy[sy][sx] = 'S'

    if end:
        ex, ey = end
        maze_copy[ey][ex] = 'E'

    if pos:
        x, y = pos
        maze_copy[y][x] = 'O'  # titik bergerak

    for row in maze_copy:
        print(''.join(row))

# Clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# MAIN
maze = generate_maze(WIDTH, HEIGHT)
start = (1, 1)
end = (WIDTH-2, HEIGHT-2)

path = solve_maze(maze, start, end)

# Animasi pergerakan
for step in path:
    clear()
    print_maze(maze, pos=step, start=start, end=end)
    time.sleep(0.1)
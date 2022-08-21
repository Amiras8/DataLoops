import sys

import numpy as np

found = []
visited = set()
q = []


def bfs(maze):
    # Check if visited, if not -> mark visited
    while q:
        loc = q.pop(0)
        x = loc[0]
        y = loc[1]
        depth = loc[2]
        if not ((x, y) in visited):

            # Found ghost
            if maze[x][y] == 2:
                found.append([(x, y), depth])

            # Invalid tiles
            if maze[x][y] != 1:
                # check for boundries and add to queue
                if x > 0:
                    q.append((x - 1, y, depth + 1))
                if x < len(maze) - 1:
                    q.append((x + 1, y, depth + 1))
                if y > 0:
                    q.append((x, y - 1, depth + 1))
                if y < len(maze[0]) - 1:
                    q.append((x, y + 1, depth + 1))

            # mark visited
            visited.add((x, y))

    # if x > 0:
    #     bfs(maze=maze, x=x - 1, y=y, depth=depth + 1)
    # if x < len(maze)-1:
    #     bfs(maze=maze, x=x + 1, y=y, depth=depth + 1)
    # if y > 0:
    #     bfs(maze=maze, x=x, y=y - 1, depth=depth + 1)
    # if y < len(maze[0])-1:
    #     bfs(maze=maze, x=x, y=y + 1, depth=depth + 1)


def SearchFromPoint(maze, initialx, initialy):
    q.append((initialx, initialy, 0))
    bfs(maze)


def findPacman(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == 3):
                return i, j
    return None


if __name__ == '__main__':
    board = None
    args = sys.argv[1:]
    if (args[0] == "--board"):
        board = np.load(args[1], allow_pickle=True)
    x, y = findPacman(board)
    SearchFromPoint(maze=board, initialx=x, initialy=y)
    print(found)

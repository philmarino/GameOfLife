def gameOfLife(board):
    result = []
    for i in range(len(board)):
        result.append([])
        for j in range(len(board[0])):
            score = liveNeighbors(board, i, j)
            #1 Any live cell with fewer than two live neighbors dies as if caused by under-population.
            if board[i][j] == 1 and score < 2:
                result[i].append(0)
                continue
            #2 Any live cell with two or three live neighbors lives on to the next generation.
            if board[i][j] == 1 and (score == 2 or score == 3):
                result[i].append(1)
                continue
            #3 Any live cell with more than three live neighbors dies, as if by over-population.
            if board[i][j] == 1 and score > 3:
                result[i].append(0)
                continue
            #4 Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            if board[i][j] == 0 and score == 3:
                result[i].append(1)
                continue
            
            result[i].append(0) #dead stays dead

    return result

def liveNeighbors(board, x, y):
    result = 0

    #NW
    if x > 0 and y > 0:
        result += board[x-1][y-1]
    #N
    if y > 0:
        result += board[x][y-1]
    #NE
    if x+1 < len(board) and y > 0:
        result += board[x+1][y-1]
    #W
    if x > 0:
        result += board[x-1][y]
    #E
    if x+1 < len(board):
        result += board[x+1][y]
    #SW
    if x > 0 and y+1 < len(board[0]):
        result += board[x-1][y+1]
    #S
    if y+1 < len(board[0]):
        result += board[x][y+1]
    #SE
    if x+1 < len(board) and y+1 < len(board[0]):
        result += board[x+1][y+1]
    return result

# Example 1:
# Input: 
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(gameOfLife(board))
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

# Example 2:
# Input: 
board = [[1,1],[1,0]]
print(gameOfLife(board))
# Output: [[1,1],[1,1]]
 

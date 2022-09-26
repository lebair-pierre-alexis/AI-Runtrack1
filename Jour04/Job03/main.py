def checkPos(board, row, col, map_size):
    for i in range(col):
        if board[row][i] == "X":
            return False
    for i, j in zip(range(row, -1, -1), 
                    range(col, -1, -1)):
        if board[i][j] == "X":
            return False
    for i, j in zip(range(row, map_size, 1), 
                    range(col, -1, -1)):
        if board[i][j] == "X":
            return False
    return True

def placeQueens(board, map_size, col):
    if col >= map_size:
        return True
    for i in range(map_size):
        if checkPos(board, i, col, map_size):
            board[i][col] = "X"
            if placeQueens(board, map_size, col + 1) == True:
                return True
        board[i][col] = "O"
    return False

map_size = input("Entrez la taille du plateau : ")
while map_size.isdigit() == False:
    map_size = input("Entrez une taille de plateau valide : ")

map_size = int(map_size)
board = [["O"] * map_size for i in range(map_size)]
if placeQueens(board, map_size, 0) == False:
    print("Aucune solution")
else:    
    for line in board:
        tab = ""
        for e in line:
            tab += e
        print(tab)

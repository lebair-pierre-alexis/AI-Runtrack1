import numpy as np

class   Board:

    def __init__(self, i, j) -> None:
        self._board = np.zeros((i, j), dtype=np.int16)
        self._height = i
        self._width = j

    def play(self, pos, color) -> bool:
        if pos < 0 or pos >= self._width:
            print("Selectionez une colonne valide !")
            return (False)
        for i in range(self._height - 1, -1, -1):
            if self._board[i][pos] == 0:
                self._place(i, pos, color)
                return True
            if i == 0:
                print("Plus de place dans cette colonne !")
                return False

    def printBoard(self):
        print(" _" * (self._width + 1))
        for x in range(0, self._height):
            if x == self._height - 1:
                text = "|_"
            else:
                text = "| "
            for y in range(0, self._width):
                if x == self._height - 1:
                    text = text + self._getColor(x, y) + "_"
                else:  
                    text = text + self._getColor(x, y) + " "
            text = text + "|"
            print(text)
        print("\n")

    def _checkWin(self):
        for x in range(self._height - 1, -1, -1):
            for y in range(0, self._width):
                if self._getColor(x, y) != "O":
                    if self._checkNext(x, y, "diag") or self._checkNext(x, y, "col") or self._checkNext(x, y, "line") or self._checkNext(x, y, "diag2"):
                        self.printBoard()
                        if self._getColor(x, y) == "R":
                            print("Le joueur Rouge à gagné félicitation !")
                        else:
                            print("Le joueur Jaune à gagné félicitation !")
                        return True
                    pass
        return False

    def _checkNext(self, posx, posy, dir, count = 1):
        if count == 4:
            return True
        if dir == "diag":
            if posx - 1 < self._height and posy + 1 < self._width and self._getColor(posx - 1, posy + 1) == self._getColor(posx, posy):
                return self._checkNext(posx - 1, posy + 1, dir, count + 1)
            return False
        if dir == "diag2":
            if posx - 1 < self._height and posy - 1 > -1 and self._getColor(posx - 1, posy - 1) == self._getColor(posx, posy):
                return self._checkNext(posx - 1, posy - 1, dir, count + 1)
            return False
        if dir == "col":
            if posx - 1 < self._height and self._getColor(posx - 1, posy) == self._getColor(posx, posy):
                    return self._checkNext(posx - 1, posy, dir, count + 1)
            return False
        if dir == "line":
            if posy + 1 < self._width and self._getColor(posx, posy + 1) == self._getColor(posx, posy):
                    return self._checkNext(posx, posy + 1, dir, count + 1)
            return False
    def _place(self, x, y, color):
        self._board[x][y] = color

    def _getColor(self, x, y):
        if self._board[x][y] == 0:
            return "O"
        elif self._board[x][y] == 1:
            return "R"
        else:
            return "J"

#driver code
valid = False
while valid == False:
    x = input("Entrez la hauteur du plateau de jeu : ")
    while x.isdigit() != True:
        x = input("Entrez une hauteur de plateau valide ! : ")
    y = input("Entrer la largeur du plateau de jeu : ")
    while y.isdigit() != True:
        y = input("Entrez une largeur de plateau valide ! : ")
    if int(x) < 4 or int(y) < 4:
        print("Il faut que la plateau face 4x4 minimum")
    else:
        valid = True
board = Board(int(x), int(y))
i = 1
while board._checkWin() != True:
    board.printBoard()
    pos = -1
    while pos == -1 or board.play(int(pos) - 1, i) == False:
        if i == 1:
            pos = input("Tour du Joueur Rouge, choisissez une colonne : ")
        else:
            pos = input("Tour du Joueur Jaune, choisissez une colonne : ")
        while pos.isdigit() == False:
            board.printBoard()
            pos = input("Entrez un numéro de colonne valide ! :")
    i = i % 2 + 1
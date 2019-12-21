def drawBoard(board):
    line = ("-" * 3 + " ")
    print("  ", end="")
    for x in range(1, board + 1):
        print(f"  {x} ", end="")
    print()
    y = 0
    for x in range(0, board):
        print(f"   {line * board}")
        print(f"{alphabet[x]} |", end="")
        for y in range(0, board):
            print(f" {gameBoard[x][y]} |", end="")
        print()
    print(f"   {line * board}")


def searchPlace(letter):
    s = letter[0].capitalize()
    return alphabet.find(s)


def winSearcher():
    win = 0
    for y in range(0, boardSize):
        win = 0
        for x in range(0, boardSize):
            if gameBoard[x][y] == "X":
                win += 1
            if win == boardSize:
                print("X is the winner!")
                return win

    for y in range(0, boardSize):
        win = 0
        for x in range(0, boardSize):
            if gameBoard[y][x] == "X":
                win += 1
            if win == boardSize:
                print("X is the winner!")
                return win

    for y in range(0, boardSize):
        win = 0
        for x in range(0, boardSize):
            if gameBoard[x][y] == "O":
                win += 1
            if win == boardSize:
                print("O is the winner!")
                return win

    for y in range(0, boardSize):
        win = 0
        for x in range(0, boardSize):
            if gameBoard[y][x] == "O":
                win += 1
            if win == boardSize:
                print("O is the winner!")
                return win

    if win != boardSize:
        win = 0
    for y in range(0, boardSize):
        if gameBoard[y][y] == "O":
            win += 1
        if win == boardSize:
            print("O is the winner!")
            return win

    if win != boardSize:
        win = 0
    for y in range(0, boardSize):
        if gameBoard[y][y] == "X":
            win += 1
        if win == boardSize:
            print("X is the winner!")
            return win

    if win != boardSize:
        win = 0
    for y in range(0, boardSize):
        if gameBoard[y][boardSize - y - 1] == "O":
            win += 1
        if win == boardSize:
            print("O is the winner!")
            return win

    if win != boardSize:
        win = 0
    for y in range(0, boardSize):
        if gameBoard[y][boardSize - y - 1] == "X":
            win += 1
        if win == boardSize:
            print("X is the winner!")
            return win


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    boardSize = input("Please chose a board size, max 26: ")
    if boardSize.isdigit() and 0 < int(boardSize) <= 26:
        boardSize = int(boardSize)
        gameBoard = [[" "] * boardSize for i in range(0, boardSize)]
        print()
        drawBoard(boardSize)
        tries = 0
        break
    else:
        print("Wrong choice! Try again.")

print("\nLET'S PLAY A GAME\n")

while tries != boardSize ** 2:

    while tries != boardSize ** 2:
        X = input("Pick the place for X: ")
        if X[0].isalpha() and X[1:].isdigit() and int(X[1:]) <= boardSize:
            if gameBoard[searchPlace(X[0])][int(X[1:]) - 1] == " ":
                gameBoard[searchPlace(X[0])][int(X[1:]) - 1] = "X"
                tries += 1
                break
            else:
                print("This place is already taken, try again")
        else:
            print("Error, try again!")

    print("\n!~ ACTUAL GAME BOARD ~!\n")

    drawBoard(boardSize)
    print()
    if winSearcher() == boardSize:
        break

    while tries != boardSize ** 2:
        O = input("Pick the place for O: ")
        if O[0].isalpha() and O[1:].isdigit() and int(O[1:]) <= boardSize:
            if gameBoard[searchPlace(O[0])][int(O[1:]) - 1] == " ":
                gameBoard[searchPlace(O[0])][int(O[1:]) - 1] = "O"
                tries += 1
                break
            else:
                print("This place is already taken, try again")
        else:
            print("Error, try again!")

    print("\n!~ ACTUAL GAME BOARD ~!\n")

    drawBoard(boardSize)
    print()
    if winSearcher() == boardSize:
        break

    if tries == boardSize ** 2:
        print("Draw!")

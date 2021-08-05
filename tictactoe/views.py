from django.shortcuts import render
from random import randrange

# Create your views here.
def tictactoe(request):
    board = [""] * 9 + ["X"]
    with open("board.txt", "w") as f:
        f.write(" ".join(board))
    return square_click(request)


def square_click(request):
    with open("board.txt", "r") as f:
        board = f.readline().split(" ")
    if "first-toggle" in request.POST:
        board = [""] * 9 + ["O" if board[-1] == "X" else "X"]
    winCheck = detectWin(board)
    if winCheck == "":
        for i in range(9):
            if "box" + str(i) in request.POST and board[i] == "":
                board[i] = "X"

    if winCheck == "" and (board[-1] == "O" or "".join(board) != "X"):
        board = makeMove(board)
    winCheck = detectWin(board)
    with open("board.txt", "w") as f:
        f.write(" ".join(board))

    boardContext = {"sq" + str(i): board[i] for i in range(9)}
    boardContext["win"] = winCheck
    boardContext["first"] = board[-1]
    return render(request, "tictactoe/tictactoe.html", boardContext)


def detectWin(board):
    # Check Rows
    sets = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for i, j, k in sets:
        a, b, c = board[i], board[j], board[k]
        if (a == "X" or a == "O") and a == b and a == c:
            return a
    return ""


def makeMove(board):
    empties = [i for i in range(9) if board[i] == ""]
    print(empties)
    if len(empties) == 0:
        return board
    index = randrange(len(empties))
    board[empties[index]] = "O"
    return board

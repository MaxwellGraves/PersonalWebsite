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
    if detect_win(board):
        return render_board(request, board)
    validSquare = False
    for i in range(9):
        if "box" + str(i) in request.POST and board[i] == "":
            board[i] = "X"
            validSquare = True

    if validSquare:
        board = make_move(board)

    with open("board.txt", "w") as f:
        f.write(" ".join(board))

    return render_board(request, board)


def change_first(request):
    with open("board.txt", "r") as f:
        board = f.readline().split(" ")
    board = [""] * 9 + ["X" if board[-1] == "O" else "O"]
    if board[-1] == "O":
        board = make_move(board)
    with open("board.txt", "w") as f:
        f.write(" ".join(board))
    return render_board(request, board)


def new_game(request):
    with open("board.txt", "r") as f:
        board = f.readline().split(" ")
    board = [""] * 9 + [board[-1]]
    if board[-1] == "O":
        board = make_move(board)
    with open("board.txt", "w") as f:
        f.write(" ".join(board))
    return render_board(request, board)


def render_board(request, board):
    boardContext = {"sq" + str(i): board[i] for i in range(9)}
    boardContext["win"] = detect_win(board)
    boardContext["first"] = board[-1]
    return render(request, "tictactoe/tictactoe.html", boardContext)


def detect_win(board):
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


def make_move(board):
    empties = [i for i in range(9) if board[i] == ""]
    print(empties)
    if len(empties) == 0:
        return board
    index = randrange(len(empties))
    board[empties[index]] = "O"
    return board

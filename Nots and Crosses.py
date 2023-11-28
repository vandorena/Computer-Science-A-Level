
board = [[-1,-1,-1,],[-1,-1,-1],[-1,-1,-1]]
move_counter = 0
current_move = 0

def board_displayer(a,b):
    if board[a][b] == -1:
        return "   "
    elif board[a][b] == 0:
        return " o "
    elif board[a][b] == 1:
        return " x "

def print_board():
    print(f"Collums: 1  2   3")
    print(f"Row 1: {board_displayer(0,0)}|{board_displayer(0,1)}|{board_displayer(0,2)}")
    print(f"       -----------")
    print(f"Row 2: {board_displayer(1,0)}|{board_displayer(1,1)}|{board_displayer(1,2)}")
    print(f"       -----------")
    print(f"Row 3  {board_displayer(2,0)}|{board_displayer(2,1)}|{board_displayer(2,2)}")

def test_function():
    if board_displayer(0,0) == board_displayer(0,1) and board_displayer(0,1) == board_displayer(0,2) and board_displayer(0,0) != "  ":
        if board_displayer(0,0) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(1,0) == board_displayer(1,1) and board_displayer(1,1) == board_displayer(0,2) and board_displayer(1,0) != "  ":
        if board_displayer(1,0) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(2,0) == board_displayer(2,1) and board_displayer(2,1) == board_displayer(2,2) and board_displayer(2,0) != "  ":
        if board_displayer(2,0) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(0,0) == board_displayer(1,1) and board_displayer(1,1) == board_displayer(2,2) and board_displayer(0,0) != "  ":
        if board_displayer(0,0) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(0,0) == board_displayer(1,0) and board_displayer(1,0) == board_displayer(2,0) and board_displayer(0,0) != "  ":
        if board_displayer(0,0) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(0,1) == board_displayer(1,1) and board_displayer(1,1) == board_displayer(2,1) and board_displayer(0,1) != "  ":
        if board_displayer(0,1) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(0,2) == board_displayer(1,2) and board_displayer(1,2) == board_displayer(2,2) and board_displayer(1,2) != "  ":
        if board_displayer(0,2) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(0,2) == board_displayer(1,1) and board_displayer(1,1) == board_displayer(2,0) and board_displayer(0,2) != "  ":
        if board_displayer(0,2) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    else:
        return "nothing"

print_board()

def test_true():
    if test_function() == "nothing":
        return True
    else:
        return False

def current_move_display():
    if move_counter % 2 == 1:
        return "X"
    else:
        return "O"

def take_turn():
    print(f"It is {current_move_display()}'s turn now:")
    print(f"Please enter the tile you would like to move to, by first entering the Row, and then entering the collum: ")
    row_holder = False
    while not row_holder:
        row = input("Input the Row Number: ")
        try:
            row_int = int(row)
        except ValueError:
            row_int = -1
        if row_int < 1 or row_int > 3:
            row_holder = False
        else:
            row_holder = True
    col_holder = False
    while not col_holder:
        col = input("Input the Collum Number: ")
        try:
            col_int = int(col)
        except ValueError:
            col_int = -1
        if col_int < 1 or col_int > 3:
            col_holder = False
        else:
            col_holder = True
    move_counter = move_counter + 1
    return f"{row_int-1}{col_int-1}"
    
def game_on():
    while test_true():
        print_board()
        move = take_turn()
        if current_move_display() == "X":
            player = 1
        else:
            player = 0


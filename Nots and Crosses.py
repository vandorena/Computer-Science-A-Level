import datetime
import random

board = [[-1,-1,-1,],[-1,-1,-1],[-1,-1,-1]]
valid_move_list = []

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
    if board_displayer(0,0) == board_displayer(0,1) and board_displayer(0,1) == board_displayer(0,2) and board[0][0] != -1 :
        if board_displayer(0,0) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(1,0) == board_displayer(1,1) and board_displayer(1,1) == board_displayer(0,2) and board[1][0] != -1 :
        if board_displayer(1,0) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(2,0) == board_displayer(2,1) and board_displayer(2,1) == board_displayer(2,2) and board[2][0] != -1 :
        if board_displayer(2,0) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(0,0) == board_displayer(1,1) and board_displayer(1,1) == board_displayer(2,2) and board[0][0] != -1 :
        if board_displayer(0,0) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(0,0) == board_displayer(1,0) and board_displayer(1,0) == board_displayer(2,0) and board[0][0] != -1 :
        if board_displayer(0,0) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(0,1) == board_displayer(1,1) and board_displayer(1,1) == board_displayer(2,1) and board[0][1] != -1 :
        if board_displayer(0,1) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(0,2) == board_displayer(1,2) and board_displayer(1,2) == board_displayer(2,2) and board[1][2] != -1 :
        if board_displayer(0,2) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    elif board_displayer(0,2) == board_displayer(1,1) and board_displayer(1,1) == board_displayer(2,0) and board[0][2] != -1 :
        if board_displayer(0,2) == "x ":
            return "winner is crosses"
        else:
            return "winner is knots"
    else:
        return "nothing"

def test_true():
    if test_function() != "nothing":
        return True
    else:
        return False

def current_move_display(move_counter):
    if move_counter % 2 == 1:
        return "X"
    else:
        return "O"

def take_turn(move_counter):
    print(f"It is {current_move_display(move_counter)}'s turn now:")
    print(f"Please enter the tile you would like to move to, by first entering the Row, and then entering the collum: ")
    entry_holder = False
    row_holder = False
    while not entry_holder:
        while not row_holder:
            row = input("Input the Row Number: ")
            try:
                row_int = int(row)
            except ValueError:
                row_int = -1
            if row_int > 0 and row_int < 4 and len(row) == 1:
                row_holder = True
            else:
                row_holder = False
        col_holder = False
        while not col_holder:
            col = input("Input the Collum Number: ")
            try:
                col_int = int(col)
            except ValueError:
                col_int = -1
            if col_int < 4 and col_int > 0 and len(col) == 1:
                col_holder = True
            else:
                col_holder = False
        if board[int(row_int-1)][int(col_int-1)] == -1:
            entry_holder = True
    
    return f"{row_int-1}{col_int-1}"
    
def game_on():
    current_move = 0
    move_counter = 0
    test_true_check = True
    while test_true_check == True:
        print_board()
        move = take_turn(move_counter)
        if current_move_display(move_counter) == "X":
            player = 1
        else:
            player = 0
        board[int(move[0])][int(move[1])] = player
        move_counter = move_counter + 1
        game_state = test_function()
        if game_state != "nothing":
            test_true_check = False
    print("-----------------------------------------")
    for i in range (0,3):
        print("")
    print(f"{game_state}")
    print_board()
    save_state_option_holder = False
    while not save_state_option_holder:
        save_state_option_integer = -1
        print("Do you want to save this game?")
        print("Enter 1 to save or 2 to discard and go back to menu.")
        save_state_option = input("")
        try:
            save_state_option_integer = int(save_state_option)
            if len(save_state_option) == 1 and save_state_option_integer > 0 and save_state_option_integer < 3:
                save_state_option_holder = True
        except ValueError:
            save_state_option_integer = -1
    if save_state_option_integer == 1:
        storefile = open(f"nots_crosses_game.txt","a")
        storefile.write("\n")
        storefile.write(f"--- Game at {datetime.datetime.today()} ---")
        storefile.write("\n")
        storefile.write("Collums: 1  2   3")
        storefile.write("\n")
        storefile.write(f"Row 1: {board_displayer(0,0)}|{board_displayer(0,1)}|{board_displayer(0,2)}")
        storefile.write("\n")
        storefile.write("       -----------")
        storefile.write("\n")
        storefile.write(f"Row 2: {board_displayer(1,0)}|{board_displayer(1,1)}|{board_displayer(1,2)}")
        storefile.write("\n")
        storefile.write("       -----------")
        storefile.write("\n")
        storefile.write(f"Row 3: {board_displayer(2,0)}|{board_displayer(2,1)}|{board_displayer(2,2)}")
        storefile.write("\n")
        storefile.write("\n")

def display_file():
    try:
        storefile = open("nots_crosses_game.txt","r")
        print(storefile.read())
    except FileNotFoundError:
        print("File not found, save some games first")
        print("")

def side_player_choice():
    side_choice_holder = False
    while not side_choice_holder:
        print("To be X's enter 1 to be O's enter 2")
        side_choice_input =  input("")
        if len(side_choice_input) == 1:
            int_side_choice_input = int(side_choice_input)
            if int_side_choice_input > 2 or int_side_choice_input <1:
                side_choice_holder = False
            else:
                side_choice_holder = True
    if int_side_choice_input == 1:
        return 1
    elif int_side_choice_input == 2:
        return 0
    
def ai_turn(valid_move_list):
    for i in range(0,2):
        for j in range(0,2):
            if board[i][j] == -1:
                valid_move_list.append([i,j])
    try:
        chosen_value = valid_move_list[random.randint(0,len(valid_move_list))]
    except IndexError:
        chosen_value = valid_move_list[random.randint(0,len(valid_move_list-1))]
    valid_move_list = []
    return chosen_value
            

def ai_game_on():
    player = side_player_choice()
    if player == 1:
        computer = 0
    else:
        computer = 1
    current_move = 0
    move_counter = 0
    test_true_check = True
    while test_true_check == True:
        print_board()
        if move_counter % 2 == 1:
            move = ai_turn(valid_move_list)
            board[move[0]][move[1]] = computer
        else:
            move = take_turn(move_counter)
            board[int(move[0])][int(move[1])] = player
        move_counter = move_counter + 1
        game_state = test_function()
        if game_state != "nothing":
            test_true_check = False
    print("-----------------------------------------")
    for i in range (0,3):
        print("")
    print(f"{game_state}")
    print_board()
    save_state_option_holder = False
    while not save_state_option_holder:
        save_state_option_integer = -1
        print("Do you want to save this game?")
        print("Enter 1 to save or 2 to discard and go back to menu.")
        save_state_option = input("")
        try:
            save_state_option_integer = int(save_state_option)
            if len(save_state_option) == 1 and save_state_option_integer > 0 and save_state_option_integer < 3:
                save_state_option_holder = True
        except ValueError:
            save_state_option_integer = -1
    if save_state_option_integer == 1:
        if computer == 1:
            ai_side = "X"
            player_side = "O"
        else:
            ai_side = "O"
            player_side = "X"
        storefile = open(f"nots_crosses_game.txt","a")
        storefile.write("\n")
        storefile.write(f"--- Game vs AI at {datetime.datetime.today()} Ai was {ai_side} and you were {player_side} ---")
        storefile.write("\n")
        storefile.write("Collums: 1  2   3")
        storefile.write("\n")
        storefile.write(f"Row 1: {board_displayer(0,0)}|{board_displayer(0,1)}|{board_displayer(0,2)}")
        storefile.write("\n")
        storefile.write("       -----------")
        storefile.write("\n")
        storefile.write(f"Row 2: {board_displayer(1,0)}|{board_displayer(1,1)}|{board_displayer(1,2)}")
        storefile.write("\n")
        storefile.write("       -----------")
        storefile.write("\n")
        storefile.write(f"Row 3: {board_displayer(2,0)}|{board_displayer(2,1)}|{board_displayer(2,2)}")
        storefile.write("\n")
        storefile.write("\n")

def runtime_menu():
    runtime_menu_exit_holder = False
    spacer = 15
    while not runtime_menu_exit_holder:
        runtime_menu_option_holder = False
        while not runtime_menu_option_holder:
            runtime_menu_option_integer = -1
            for i in range(0,spacer):
                print("")
            print("Select from the following options by inputing an integer: ")
            print("1. Start a New Game")
            print("2. Play Against a Computer")
            print("3. View Saved Games")
            print("4. Clear Saved Games")
            print("5. Exit")
            print("")
            runtime_menu_option = input("")
            try:
                runtime_menu_option_integer = int(runtime_menu_option)
                if len(runtime_menu_option) == 1 and runtime_menu_option_integer > 0 and runtime_menu_option_integer < 5:
                    runtime_menu_option_holder = True
            except ValueError:
                runtime_menu_option_integer = -1
        if runtime_menu_option_integer == 1:
            game_on()
            spacer = 3
        elif runtime_menu_option_integer == 2:
            ai_game_on()
        elif runtime_menu_option_integer == 3:
            display_file()
            spacer = 1
        elif runtime_menu_option_integer == 4:
            file_to_delete = open("nots_crosses_game.txt",'w')
            file_to_delete.close()
            spacer = 15
        elif runtime_menu_option_integer == 5:
            runtime_menu_exit_holder = True

# currently got a logic error in the AI side.
runtime_menu()
import sys
import random




def start_game():
    print("""\n
                             Welcome to the game:
#######             #######                  #######               
   #    #  ####        #      ##    ####        #     ####  ###### 
   #    # #    #       #     #  #  #    #       #    #    # #      
   #    # #            #    #    # #            #    #    # #####  
   #    # #            #    ###### #            #    #    # #      
   #    # #    #       #    #    # #    #       #    #    # #      
   #    #  ####        #    #    #  ####        #     ####  ######  
   \n                                                
            Hello everybody! You need choice game options to start the game.
                                GOOD LUCK! """)



def init_board(): # dwie wersje
    board = [['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3']] 
    for row in range(len(board)):
        for col in range(len(board)):
            board[row][col] = "."
    return board


    # for row in board:
    #     for dots in row:
    #         print(dots, end="")
    #     print()



def is_full(board): #Check for a full board
# do poprawy , w naszym przypadku element to [" "," "," "]
    is_full = True
    for elements in board:
        if elements == ".":
            is_full = False
    return is_full
    


def print_result(winner): 
    if winner == 10:
        print("It's a tie")
    else:
        if winner%2 == 1:
            print("O has won!")
        else:
            print("X has won!")
   

def get_move(board, player): # do naprawienia błąd jeśli drugi znak nie jest liczbą
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0 
    print("Podaj współrzędne na których umiescisz swój znak:",player)
    input_user = input()
    input_user = input_user.lower()
    if input_user == 'quit':
        print("Do zobaczenia !!!")
        sys.exit()
    elif len(input_user) != 2:
        print("Podałeś niewłaściwą ilość znaków")
        get_move(board,player)
    else :
        row = input_user[0]
        col = int(input_user[1])-1
    
    if row == "a":
        row = 0
    elif row == "b":
        row = 1
    elif row == "c":
        row = 2
    
    if input_user not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]:
        print("Podałeś złe współrzędne, spróbuj jeszcze raz : ")
        row,col = get_move(board, player)
    elif board[row][col] != ".":
        print("Podałeś współrzędne na których już znajduje się jakiś znak : ")
        row,col = get_move(board, player)
    
    return row, col

def get_ai_move(board,player):
    """generuje ruch komputera w zalezności od wybranych opcji"""
    good = False
    hot_place =[[".","."]]
    test_mark = player
    if find_hot(board,test_mark,hot_place) is False:
        if test_mark == "x":
            test_mark ="o"
        else :
            test_mark = "x"
        find_hot(board,test_mark,hot_place)
    while good == False:
        if hot_place[0] != [[".","."]]:
            row = int(hot_place[0][0])
            col = int(hot_place[0][1])
            good = True
        else :
            chose=[0,0]
            chose[0]=random.randint(0,2)
            chose[1]=random.randint(0,2)
            if board[chose[0]][chose[1]] == ".":
                row = int(chose[0])
                col = int(chose[1])
                good = True
            else :
                pass

    print("The computer chose: ",row,col)
    return row,col  

def find_hot(board,player,hot_place):
    """Znajduje linie z  dwoma takimi samymi znakami jako szanse do ataku lub obronę"""
    for i in range (0,3):
        result =0
        temp = [[".","."]]      
        for j in range (0,3):            
            if board[i][j] == player:
                result += 1
            if board[i][j] == ".":
                temp[0] = (i,j)                
        if result == 2 and temp != [[".","."]]:
            hot_place[0] = temp[0]
            return True
            
    for i in range (0,3):        
        result =0
        temp = [[".","."]]
        for j in range (0,3):            
            if board[j][i] == player:
                result += 1
            if board[j][i] == ".":
                temp[0] = (j,i)                
        if result == 2 and temp != [[".","."]]:
            hot_place[0] = temp[0]
            return True
    
    result = 0
    temp = [[".","."]]
    for i in range (0,3):
        if board[i][i] == player:
            result += 1
        if board[i][i] == ".":
            temp[0] = (i,i)            
    if result == 2 and temp != [[".","."]]:
        hot_place[0] = temp[0]
        return True

    result = 0
    j = 2
    temp = [[".","."]]
    for i in range (0,3):
        if board[i][j] == player:
            result += 1
        if board[i][j] == ".":
            temp[0] = (i,j)            
        j -= 1
    if result == 2 and temp != [[".","."]]:
        hot_place[0] = temp[0]
        return True
    hot_place[0] = [[".","."]]  
    return False        

def has_won(board,player): #dlaczego na starcie jest False?
    
    for i in range (0,3):
        result =0
        for j in range (0,3):
            if board[i][j] == player:
                result += 1
            if result == 3:
                return True
            
    for i in range (0,3):
        result =0
        for j in range (0,3):
            if board[j][i] == player:
                result += 1
            if result == 3:
                return True
    result = 0
    for i in range (0,3):
        if board[i][i] == player:
            result += 1
        if result == 3:
                return True
    result = 0
    j = 2
    for i in range (0,3):
        if board[i][j] == player:
            result += 1
        if result == 3:
            return True
        j -= 1
    return False

def mark(board, player, row, col):
    """wstawia o lub x do współrzędnych na tablicy"""
    board[row][col] = player

def print_board(board):
    print("   1    2    3")
    print("A ",board[0][0],"| ",board[0][1],"| ",board[0][2])
    print("--------------")
    print("B ",board[1][0],"| ",board[1][1],"| ",board[1][2])
    print("--------------")
    print("C ",board[2][0],"| ",board[2][1],"| ",board[2][2])

def tictactoe_game(option):
    board  = init_board() #funkcja init_board ma utworzyć tablicę board,powinna nie pobierać parametrów a jedynie zwracać tablicę
    print_board(board)
    player = "x"
    user_count = 1
                    
    while has_won(board, player) == False and is_full(board) == True :
        if option == 1:        
            if user_count % 2 == 1:
                player = 'x'
                row,col = get_move(board, player)
            else:
                player = 'o'
                row,col = get_move(board,player)
        
        elif option == 2 :                        
            if user_count%2 == 1:
                player = 'x'
                row,col = get_ai_move(board, player)
            else:
                player = 'o'
                row,col = get_move(board,player)
        mark(board, player, row, col)# funkcja dodaje znak do istniejącej tablicy
        print_board(board)
        user_count += 1
    print_result(user_count)



def main_menu():
    input_check = False
    while input_check is False:
        while True:
            try :
                option = int(input("""
                Select game options: 
                1 - 2 player mode or 
                2 - player against AI mode
                """))
                break
            except ValueError :
                print("You must give a integer number")
                continue
        if option > 0 and option <= 3:
            input_check= True
        else:
            print("You entered a number out of range. Please try again.")
    return option

    

def main():
    start_game()
    option = main_menu()
    tictactoe_game(option)
    

if __name__ == "__main__":
   
    main()
    






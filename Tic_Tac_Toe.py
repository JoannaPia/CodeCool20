x = "x"
o = "o"
dots = "."

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
            Hello everybody! You need choice "x" or "o" to start the game.
                                GOOD LUCK! """)

    init_board(9)

    
def init_board(number): # w nawiasie zmienna, którą mozemy zmieniać
    dots = "."
    square = number

    board = []
    for square in range(square):
        board.append(dots)


    print("\n\t", "1""  "  , "2""  " ,  "3" )
    print("\n\t""A" , board[0], "|", board[1], "|", board[2])
    print("\t",   "---------")
    print("\t""B", board[3], "|", board[4], "|", board[5])
    print("\t",   "---------")
    print("\t""C", board[6], "|", board[7], "|", board[8], "\n")

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
        col = int(input_user[1])
    
    if row == "a":
        row = 0
    elif row == "b":
        row = 1
    elif row == "c":
        row = 2
    
    if input_user not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]:
        print("Podałeś złe współrzędne, spróbuj jeszcze raz : ")
        row,col = get_move(board, player)
    elif board[row][col-1] != ".":
        print("Podałeś współrzędne na których już znajduje się jakiś znak : ")
        row,col = get_move(board, player)
    
    return row, col

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


#Print result
#Check for a full board

def main():
    start_game()
    making_a_move()
    
    

if __name__ == "__main__":
    main()







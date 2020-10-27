x = "x"
o = "o"

board = ['.','.','.','.','.','.','.','.','.']

total_moves = 0


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
    question_start_game()

    
def init_board(number): # w nawiasie zmienna, którą mozemy zmieniać
    


    board = {
    'A1': '.', 'A2': '.', 'A3': '.',
    'B1': '.', 'B2': '.', 'B3': '.',
    'C1': '.', 'C2': '.', 'C3': '.',
    }


    print("\n\t", "1""  "  , "2""  " ,  "3" )
    print("\n\t""A" , board['A1'], "|", board['A2'], "|", board['A3'])
    print("\t",   "---------")
    print("\t""B", board['B1'], "|", board['B2'], "|", board['B3'])
    print("\t",   "---------")
    print("\t""C", board['C1'], "|", board['C2'], "|", board['C3'], "\n")

def ask_yes_no(question):

    response = None
    while response not in ("yes", "no"):
        response = input(question).lower()
    return response

def question_start_game():

    computer_question = ask_yes_no("Do you want go first ? Answer yes or no:")
    if computer_question.upper() == "yes":
        print("You will start the game.")
    elif computer_question.upper() == "no":
        print("Quit")
        quit()

def ask_x_o(choice):

    response = None
    while response not in ("x", "o"):
        response = input(choice).lower()
    return response


#Implement making a move 
def making_a_move():

    user1 = ask_x_o("Now you will choice X or O: ")

    while True:
        if total_moves == 9:
            break

    while True:
        if user1.upper() == "X":
            user2 = "O"
            print("Excellent.You will be. " +  user1 + " and user2 will be " + user2 + "!")
            return user1.upper(), user2
        elif user1.upper() == "O":
            user2 = "X"
            print("Great. You will be: " + user1 + " and user2 will be " + user2 + "!")
            return user1.upper(), user2
        else:
            user1 = input("You need pick x or o. Try again.")


def is_full(board): #Check for a full board

    is_full = True
    for elements in board:
        if elements == ".":
            is_full = False
    return is_full
    


def print_result(): 
    if board['A1'] == 'X' and board['A2'] == 'X' and board['A3'] == 'X':
        print("Player one won!")
        return 1
    if board['B1'] == 'X' and board['B2'] == 'X' and board['B3'] == 'X':
        print("Player one won!")
        return 1
    if board['C1'] == 'X' and board['C2'] == 'X' and board['C3'] == 'X':
        print("Player one won!")
        return 1
    # for diagonal
    if board['A1'] == 'X' and board['B2'] == 'X' and board['C3'] == 'X':
        print("Player one won!")
        return 1 
    # for vertical
    if board['A1'] == 'X' and board['B1'] == 'X' and board['C1'] == 'X':
        print("Player one won!")
        return 1
    if board['A2'] == 'X' and board['B2'] == 'X' and board['C2'] == 'X':
        print("Player one won!")
        return 1
    if board['A3'] == 'X' and board['B3'] == 'X' and board['C3'] == 'X':
        print("Player one won!")
        return 1
      
    #checking for player 2
    if board['A1'] == 'X' and board['A2'] == 'X' and board['A3'] == 'O':
        print("Player one won!")
        return 1
    if board['B1'] == 'X' and board['B2'] == 'X' and board['B3'] == 'O':
        print("Player one won!")
        return 1
    if board['C1'] == 'X' and board['C2'] == 'X' and board['C3'] == 'O':
        print("Player one won!")
        return 1
    # for diagonal
    if board['A1'] == 'X' and board['B2'] == 'X' and board['C3'] == 'O':
        print("Player one won!")
        return 1 
    # for vertical
    if board['A1'] == 'X' and board['B1'] == 'X' and board['C1'] == 'O':
        print("Player one won!")
        return 1
    if board['A2'] == 'X' and board['B2'] == 'X' and board['C2'] == 'O':
        print("Player one won!")
        return 1
    if board['A3'] == 'X' and board['B3'] == 'X' and board['C3'] == 'O':
        print("Player one won!")
        return 1
    return 0



def main():
    start_game()
    making_a_move()
    is_full()
    
    

if __name__ == "__main__":
    main()







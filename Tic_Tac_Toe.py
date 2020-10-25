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

def ask_yes_no(question):

    response = None
    while response not in ("yes", "no"):
        response = input(question).lower()
    return response

def ask_x_o(choice):

    response = None
    while response not in ("x", "o"):
        response = input(choice).lower()
    return response


#Implement making a move 
def making_a_move():

    computer_question = ask_yes_no("Do you want go first ? Answer yes or no:")
    if computer_question.lower() == "yes":
        print("You will start the game.")

    user1 = ask_x_o("Now you will choice x or o: ")
    while True:
        if user1.lower() == "x":
            user2 = "o"
            print("Excellent.You will be" +  user1 + "User2 will be" + user2, end="")
            return user1.upper(), user2
        elif user1.upper() == "o":
            user2 = "x"
            print("Great. You will be" + user1 + "User2 will be" + user2)
            return user1.upper(), user2
        else:
            user1 = input("You need pick x or o.")





#Print result
#Check for a full board

def main():
    start_game()
    making_a_move()
    
    

if __name__ == "__main__":
    main()







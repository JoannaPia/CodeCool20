


def init_board():

    dots = "." #puste pole na planszy
    square = 9 #liczba pól na planszy

    board = [] #nowa plansza,( elementy mają wartość dots )
    for square in range(square):
        board.append(dots)


    print("\n\t",  " 1"" "  , " 2"" " ,  " 3" )
    print("\n\t""A" , board[0], "|", board[1], "|", board[2])
    print("\t",   "---------")
    print("\t""B", board[3], "|", board[4], "|", board[5])
    print("\t",   "---------")
    print("\t""C", board[6], "|", board[7], "|", board[8], "\n")


#def mark():



def main():
    init_board()

if __name__ == "__main__":
    main()







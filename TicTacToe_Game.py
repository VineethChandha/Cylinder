#PY.01.15 Project 8: Tic Tac Toe Game
#Description: It is a 2 player game where X and O are two persons symbols used to fill the board
#              If one of the person fills the board in such a way his/her symbol forms a straight line or a
#              daigonal he will be the winner


board = [" " for i in range(1,10)]      #Board with nine spaces

def printboard():                       # arrangement of board
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(symbol):

    
    print("your turn player{}".format(symbol))
          
    choice = int(input("Enter your choice from (1-9): ").strip())   # Input to give the position to enter the symbol 
    if board[choice-1] == " ":
        board[choice-1] = symbol
    else:
        print()
        print("already filled")             # if space is already used

def win(symbol):                            # checks for the sides and diagonals for the win case
    if(board[0] == symbol and board[1] == symbol and board[2] == symbol)or\
      (board[3] == symbol and board[4] == symbol and board[5] == symbol)or\
      (board[6] == symbol and board[7] == symbol and board[8] == symbol)or\
      (board[0] == symbol and board[4] == symbol and board[8] == symbol)or\
      (board[2] == symbol and board[4] == symbol and board[6] == symbol)or\
      (board[0] == symbol and board[3] == symbol and board[6] == symbol)or\
      (board[1] == symbol and board[4] == symbol and board[7] == symbol)or\
      (board[2] == symbol and board[5] == symbol and board[8] == symbol):
        print("{} wins !!!".format(symbol))
        return True
    else:
        return False
def draw():                     #if no space is remaining and the win not happens then it is a draw
    if " " not in board:
        return True
    else:
        return False
    
      
                
while True:     # used to print the table frequently
    printboard()
    player_move("X")    # Gives chance to X
    printboard()        # prints the board with X input position
    if win("X"):        # checks for win
        break           #If win happens the loop breaks
    elif draw():        # else draw
        print("Its a draw")
        break
    player_move("O")    #same as above with O
    if win("O"):
        break
    elif draw():
        print("Its a draw")
        break
    
    

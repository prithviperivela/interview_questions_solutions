def print_board(board):
    print()
    for row in range(3):
        print(""+board[row][0]+"|"+board[row][1]+"|"+board[row][2]+"")
        if row <2:
            print("_______")



def check_winner(board,player):
      for row in board:
         if  board[row][0]==board[row][1]==board[row][2]==player:
           return True
         

      for col in range(3):
         if  board[0][col]==board[1][col]==board[2][col]==player:
           return True
         
      if board[0][0]==board[1][1]==board[2][2]==player:
          return True
      if board[0][2] == board[1][1] == board[2][0] == player:
        return True
      
      return False

def check_draw(board,player):
    for i in board:
        for j in range(3):
            if board[i][j]==" ":
                return False
            
    return True

def main():
    while True:

     board=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]
     current_player="x"

      
     while True:
        try:
            print_board(board)
            a=int(input("emter a value from 1to 9 to place your mark "))
        except valueError:
            print("invalid input please enter a number between 1 to 9")
            continue
        if a<1 or a>9:
            print("invalid input please enter a number between 1 to 9")
            continue
            row = (a - 1) // 3
            col = (a - 1) % 3

            if board[row][col] != " ":
                print("Position already occupied.")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print("Player", current_player, "wins!")
                break

            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        play_again = input("Play again? (y/n): ")
        if play_again != "y":
         break

main()

        







         



   
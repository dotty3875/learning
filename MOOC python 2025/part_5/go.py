"""In a game of Go two players take turns to place black and white stones on a game board. The winner is the player who manages to encircle a bigger area on the board with their own game pieces.

Please write a function named who_won(game_board: list), which takes a two-dimensional array as its argument. The array consists of integer values, which represent the following situations:

0: empty square
1: player 1 game piece
2: player 2 game piece
The scoring rules of Go can be quite complex, but in this exercise it is enough to compare the number of pieces each player has on the game board. Also, the size of the game board is not limited.

The function should return the value 1 if player 1 won, and the value 2 if player 2 won. If both players have the same number of pieces on the board, the function should return the value 0."""

# Write your solution here
def who_won(game_board: list):
    player1 = 0
    player2 = 0
    for row in range(len(game_board)): # range finds the number of rows 
        for index in game_board[row]: # uses [row] to indicate the correct row to loop through
            if index == 1: 
                player1 += 1 
            if index == 2:
                player2 += 1
                
    if player1 == player2: # tied game - returns 0
        return 0
    elif player1 > player2: # player 1 won, so return 1 
        return 1
    elif player2 > player1: # player 2 won, so return 2 
        return 2


if __name__ == "__main__":
    who_won()
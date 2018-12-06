import numpy as np 
import random

class TicTacToeEnvironment(object):
    def __init__(self):
        self.board=np.full((3,3),2)

    def toss(self):
        """Function to simulate a toss and decide which player goes first

        Args:

        Returns:
        Returns 1 if player assigned mark 1 has won, or 0 if his opponent won

        """
        turn=np.random.randint(0,2,size=1)
        if turn.mean()==0:
            self.turn_monitor=0
        elif turn.mean()==1:
            self.turn_monitor=1
        return self.turn_monitor

    def move(self,player,coord):
        """Function to perform the action of placing a mark on the tic tac toe board
        After performing the action, this function flips the value of the turn_monitor to 
        the next player

        Args:
        player: 1 if player who is assigned the mark 1 is performing the action, 
        0 if his opponent is performing the action
        coord: The coordinate where the 1 or 0 is to be placed on the 
        tic-tac-toe board (numpy array)

        Returns:
        game_status(): Calls the game status function and returns its value
        board: Returns the new board state after making the move

        """
        if self.board[coord]!=2 or self.game_status()!="In Progress" or self.turn_monitor!=player:
            raise ValueError("Invalid move")
        self.board[coord]=player
        self.turn_monitor=1-player
        return self.game_status(),self.board


    def game_status(self):
        """Function to check the current status of the game, 
        whether the game has been won, drawn or is in progress

        Args:

        Returns:
        "Won" if the game has been won, "Drawn" if the 
        game has been drawn, or "In Progress", if the game is still in progress

        """
        #check for a win along rows
        for i in range(self.board.shape[0]):
            if 2 not in self.board[i,:] and len(set(self.board[i,:]))==1:
                return "Won"
        #check for a win along columns
        for j in range(self.board.shape[1]):
            if 2 not in self.board[:,j] and len(set(self.board[:,j]))==1:
                return "Won"
        # check for a win along diagonals
        if 2 not in np.diag(self.board) and len(set(np.diag(self.board)))==1:
            return "Won"
        if 2 not in np.diag(np.fliplr(self.board)) and len(set(np.diag(np.fliplr(self.board))))==1:
            return "Won"
        # check for a Draw
        if not 2 in self.board:
            return "Drawn"
        else:
            return "In Progress"


#Testing Environment
# from game.environment import TicTacToeEnvironment

# # create an object of the class tick_tac_toe_game
# game=tic_tac_toe_game()
# # toss to decide which player goes first
# game.toss()
# print("Player ",game.turn_monitor," has won the toss")
# # make the first move
# print("Initial board state \n",game.board)
# print("Let first player place their mark on 0,0")
# game_status,board=game.move(game.turn_monitor,(0,0))
# print("New Board State: \n",board)
# print("Let second player place their mark on 0,1")
# game_status,board=game.move(game.turn_monitor,(0,1))
# print("New Board State: \n",board)
# print("Let first player place their mark on 1,1")
# game_status,board=game.move(game.turn_monitor,(1,1))
# print("New Board State: \n",board)
# print("Let second player place their mark on 0,2")
# game_status,board=game.move(game.turn_monitor,(0,2))
# print("New Board State: \n",board)
# print("Let first player place their mark on 2,2")
# game_status,board=game.move(game.turn_monitor,(2,2))
# print("New Board State: \n",board)
# print("Player ",1-game.turn_monitor," Has ",game_status)


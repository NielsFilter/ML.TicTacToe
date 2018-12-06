def legal_moves_generator(current_board_state,turn_monitor):
    """Function that returns the set of all possible legal moves and resulting board states, 
    for a given input board state and player

    Args:
    current_board_state: The current board state
    turn_monitor: 1 if it's the player who places the mark 1's turn to play, 0 if its his opponent's turn

    Returns:
    legal_moves_dict: A dictionary of a list of possible next coordinate-resulting board state pairs
    The resulting board state is flattened to 1 d array

    """
    legal_moves_dict={}
    for i in range(current_board_state.shape[0]):
        for j in range(current_board_state.shape[1]):
            if current_board_state[i,j]==2:
                board_state_copy=current_board_state.copy()
                board_state_copy[i,j]=turn_monitor
                legal_moves_dict[(i,j)]=board_state_copy.flatten()
    return legal_moves_dict


# #testing
# import tictactoe
# import pprint
# from ticTacToeGame import tic_tac_toe_game


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

# legal_moves_dict=legal_moves_generator(game.board,game.turn_monitor)
# print("Dictionary of Possible Next Legal Moves:")
# pprint.pprint(legal_moves_dict)
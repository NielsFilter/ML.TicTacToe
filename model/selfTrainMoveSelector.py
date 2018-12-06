import game.legalMoveGen as lmg

def mutating_move_selector(model,current_board_state,turn_monitor):
 
    tracker={}
    legal_moves_dict=lmg.legal_moves_generator(current_board_state,turn_monitor)
    for legal_move_coord in legal_moves_dict:
        score=model.predict(legal_moves_dict[legal_move_coord].reshape(1,9))
        tracker[legal_move_coord]=score

# use random with higher likelihood for better scores
# np.random.choice(mode_list, 1, p=[0.5,0.5])

    selected_move=max(tracker, key=tracker.get)
    new_board_state=legal_moves_dict[selected_move]
    score=tracker[selected_move]
    return selected_move,new_board_state,score

# testing move selector
# # new game
# game=tic_tac_toe_game()
# # toss
# game.toss()
# # choose the first move
# print("Player assigned mark 1",game.turn_monitor," won the toss")
# print("Initial board state:")
# print(game.board)
# selected_move,new_board_state,score=move_selector(model,game.board,game.turn_monitor)
# print("Selected move: ",selected_move)
# print("Resulting new board state: ",new_board_state)
# print("Score assigned to above board state by Evaluator(model): ", score)
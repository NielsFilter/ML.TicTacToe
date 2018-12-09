import game.hardCodeOpponent as opp
import model.moveSelector as ms

class Opponent():
    def __init__(self, opponentIndex, preTrainedModel):
        self.opponentIndex = opponentIndex
        self.preTrainedModel = preTrainedModel
        
    def make_move(self, board, turn_monitor):
        if self.opponentIndex == 1:
            return self.make_move_easy_opp(board, turn_monitor)
        elif self.opponentIndex == 2:
            return self.make_move_hard_opp(board, turn_monitor)
        return self.make_move_nn_opp(board,turn_monitor)

    def make_move_easy_opp(self, board, turn_monitor):
        return opp.opponent_move_selector(board, turn_monitor, mode='Easy')

    def make_move_hard_opp(self, board, turn_monitor):
        return opp.opponent_move_selector(board, turn_monitor, mode='Hard')

    def make_move_nn_opp(self, board, turn_monitor):
        selected_move,new_board_state,score=ms.move_selector(self.preTrainedModel, board, turn_monitor)
        return selected_move
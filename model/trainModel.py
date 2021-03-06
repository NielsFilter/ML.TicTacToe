import numpy as np 
import pandas as pd 
import pprint,random

from scipy.ndimage.interpolation import shift
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.optimizers import SGD

from game.environment import TicTacToeEnvironment
from model.createModel import ModelCreator
import game.hardCodeOpponent as opp
import model.moveSelector as ms

#modelCreator = ModelCreator()

def train(model,mode,print_progress=False):
    game=TicTacToeEnvironment()
    game.toss()

    scores_list=[]
    corrected_scores_list=[]
    new_board_states_list=[]
    
    while(1):
        if game.game_status()=="In Progress" and game.turn_monitor==1:
            # If its the program's turn, use the Move Selector function to select the next move
            selected_move,new_board_state,score=ms.move_selector(model,game.board,game.turn_monitor)
            scores_list.append(score[0][0])
            new_board_states_list.append(new_board_state)

            # Make the next move
            game_status,board=game.move(game.turn_monitor,selected_move)

        elif game.game_status()=="In Progress" and game.turn_monitor==0:
            selected_move=opp.opponent_move_selector(game.board,game.turn_monitor,mode=mode)
        
            # Make the next move
            game_status,board=game.move(game.turn_monitor,selected_move)
        else:
            break

    
    # Correct the scores, assigning 1/0/-1 to the winning/drawn/losing final board state, 
    # and assigning the other previous board states the score of their next board state
    new_board_states_list=tuple(new_board_states_list)
    new_board_states_list=np.vstack(new_board_states_list)
    if game_status=="Won" and (1-game.turn_monitor)==1: 
        corrected_scores_list=shift(scores_list,-1,cval=1.0)
        result="Won"
    if game_status=="Won" and (1-game.turn_monitor)!=1:
        corrected_scores_list=shift(scores_list,-1,cval=-1.0)
        result="Lost"
    if game_status=="Drawn":
        corrected_scores_list=shift(scores_list,-1,cval=0.0)
        result="Drawn"
        
    x=new_board_states_list
    y=corrected_scores_list
    
    def unison_shuffled_copies(a, b):
        assert len(a) == len(b)
        p = np.random.permutation(len(a))
        return a[p], b[p]
    
    # shuffle x and y in unison
    x,y=unison_shuffled_copies(x,y)
    x=x.reshape(-1,9) 
    
    # update the weights of the model, one record at a time
    model.fit(x,y,epochs=1,batch_size=1,verbose=0)
    return model,y,result

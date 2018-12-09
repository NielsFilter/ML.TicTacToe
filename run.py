# Importing required moduless
import numpy as np 
import pandas as pd 
import pprint,random

from scipy.ndimage.interpolation import shift
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.optimizers import SGD

from game.environment import TicTacToeEnvironment
from keras.models import load_model

import model.selfTrainModel as tm
from model.createModel import ModelCreator
from game.opponent import Opponent

from random import randint

total_games = 60000
bucket_size = total_games / 20

#train lots of games
game_counter=1
data_for_graph=pd.DataFrame()

#modelToTrain = ModelCreator().PickModel("NN1")
modelToTrain = ModelCreator().LoadModel("myModel1.h5")


preTrainedModel = load_model("preTrainedOpponent.h5")

while(game_counter<= total_games):
    #mode_selected=np.random.choice([0,1,2], 1, p=[0.5,0.5,0.5])
    opponent_index = np.random.choice([0,1,2], p=[0.2,0.6,0.2]) #randint(0, 2)
    opp = Opponent(opponent_index, preTrainedModel)
    model,y,result=tm.train(modelToTrain,opp)
    data_for_graph=data_for_graph.append({"game_counter":game_counter,"result":result},ignore_index=True)

    if game_counter % bucket_size == 0:
        print("Game#: ",game_counter)
        print("Index: ",opponent_index)

    game_counter+=1


bins = np.arange(1, game_counter/bucket_size) * bucket_size
data_for_graph['game_counter_bins'] = np.digitize(data_for_graph["game_counter"], bins, right=True)
counts = data_for_graph.groupby(['game_counter_bins', 'result']).game_counter.count().unstack()
ax=counts.plot(kind='bar', stacked=True,figsize=(17,5))
ax.set_xlabel("Count of Games in Bins of 10,000s")
ax.set_ylabel("Counts of Draws/Losses/Wins")
ax.set_title('Distribution of Results Vs Count of Games Played')

print(counts)

model.save('myModel.h5')  # creates a HDF5 file 'myModel.h5's

plt.ylabel("Counts of Draws/Losses/Wins")
plt.xlabel("Count of Games in Bins of 10,000s")
plt.show()


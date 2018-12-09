import numpy as np 
import pandas as pd 
import pprint,random

from keras.models import load_model
from scipy.ndimage.interpolation import shift
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.optimizers import SGD


class ModelCreator():
    def PickModel(self, modelName):
        if modelName == "NN1":
            return self.NN1()
        else:
            return  self.NN2()

    def NN1(self):
        model = Sequential()
        model.add(Dense(18, input_dim=9,kernel_initializer='normal', activation='relu'))
        model.add(Dropout(0.1))
        model.add(Dense(9, kernel_initializer='normal',activation='relu'))
        model.add(Dropout(0.1))
        # model.add(Dense(9, kernel_initializer='normal',activation='relu'))
        # model.add(Dropout(0.1))
        # model.add(Dense(5, kernel_initializer='normal',activation='relu'))
        model.add(Dense(1,kernel_initializer='normal',activation='softmax'))

        learning_rate = 0.001
        momentum = 0.8

        sgd = SGD(lr=learning_rate, momentum=momentum,nesterov=False)
        model.compile(loss='mean_squared_error', optimizer=sgd)
        model.summary()
        return model

    def NN2(self):
        model = Sequential()
        model.add(Dense(18, input_dim=9,kernel_initializer='normal', activation='relu'))
        model.add(Dropout(0.1))
        model.add(Dense(9, kernel_initializer='normal',activation='relu'))
        model.add(Dropout(0.1))
        # model.add(Dense(9, kernel_initializer='normal',activation='relu'))
        # model.add(Dropout(0.1))
        # model.add(Dense(5, kernel_initializer='normal',activation='relu'))
        model.add(Dense(1,kernel_initializer='normal',activation='softmax'))

        learning_rate = 0.001
        momentum = 0.8

        sgd = SGD(lr=learning_rate, momentum=momentum,nesterov=False)
        model.compile(loss='mean_squared_error', optimizer=sgd)
        model.summary()
        return model
    
    def LoadModel(saveModelFileName):
        model = load_model(saveModelFileName)

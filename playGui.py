from tkinter import *
from keras.models import load_model
from game.environment import TicTacToeEnvironment
import model.moveSelector as ms

class PlayWithGui:
    def __init__(self, master):
        self.master = master
        buttonHeight = 10
        buttonWidth = 20
        master.title("Tic Tac Toe")

        Label(master, text="Take on the Machine Learning Tic Tac Toe model!").grid(columnspan=4)

        self.row0_col0 = Button(master, name="row0_col0", height = buttonHeight, width = buttonWidth, text="", command=lambda: self.makeMove(0,0))
        self.row0_col1 = Button(master, name="row0_col1", height = buttonHeight, width = buttonWidth, text="", command=lambda: self.makeMove(0,1))
        self.row0_col2 = Button(master, name="row0_col2", height = buttonHeight, width = buttonWidth, text="", command=lambda: self.makeMove(0,2))
        self.row0_col0.grid(row=1, column=0, sticky=N+S+E+W )
        self.row0_col1.grid(row=1, column=1, sticky=N+S+E+W)
        self.row0_col2.grid(row=1, column=2,sticky=N+S+E+W)

        self.row1_col0 = Button(master, name="row1_col0", height = buttonHeight, width = buttonWidth, text="", command=lambda: self.makeMove(1,0))
        self.row1_col1 = Button(master, name="row1_col1", height = buttonHeight, width = buttonWidth, text="", command=lambda: self.makeMove(1,1))
        self.row1_col2 = Button(master, name="row1_col2", height = buttonHeight, width = buttonWidth, text="", command=lambda: self.makeMove(1,2))
        self.row1_col0.grid(row=2, column=0, sticky=N+S+E+W)
        self.row1_col1.grid(row=2, column=1, sticky=N+S+E+W)
        self.row1_col2.grid(row=2, column=2, sticky=N+S+E+W)

        self.row2_col0 = Button(master, name="row2_col0", height = buttonHeight, width = buttonWidth, text="", command=lambda: self.makeMove(2,0))
        self.row2_col1 = Button(master, name="row2_col1", height = buttonHeight, width = buttonWidth, text="", command=lambda: self.makeMove(2,1))
        self.row2_col2 = Button(master, name="row2_col2", height = buttonHeight, width = buttonWidth, text="", command=lambda: self.makeMove(2,2))
        self.row2_col0.grid(row=3, column=0, sticky=N+S+E+W)
        self.row2_col1.grid(row=3, column=1, sticky=N+S+E+W)
        self.row2_col2.grid(row=3, column=2, sticky=N+S+E+W)

        self.SetHelpText("Starting game...")
        self.statusLabel = Label(master, text=self.helpText)
        self.statusLabel.grid(columnspan=4)

    def SetHelpText(self, text):
        self.helpText = text

    def PlayGame(self, model):
        self.game=TicTacToeEnvironment()
        self.game.toss()
        self.playerMarker = "O"
        self.opponentMarker = "X"

        print("{0} has won the toss".format(self.game.turn_monitor))

        self.CheckGameStatus()

    def CheckGameStatus(self):

        if self.game.game_status()=="In Progress" and self.game.turn_monitor==0:
            self.SetHelpText("Your Turn")
                
        elif self.game.game_status()=="In Progress" and self.game.turn_monitor==1:
            self.SetHelpText("Program's turn")
            chosen_move,new_board_state,score=ms.move_selector(model, self.game.board, self.game.turn_monitor)
            
            self.makeMove(chosen_move[0], chosen_move[1])
            self.CheckGameStatus()

        else:
            if self.game.game_status=="Won" and (1-self.game.turn_monitor)==1: 
                self.SetHelpText("Program has won")
            if self.game.game_status=="Won" and (1-self.game.turn_monitor)==0:
                self.SetHelpText("You have won")
            if self.game.game_status=="Drawn":
                self.SetHelpText("Game was Drawn")

    def makeMove(self, row, col, marker=""):
        # if self.game.turn_monitor==1:
        #     print("It's not your turn")
        #     return

        if marker == "":
            if self.game.turn_monitor == 1:
                marker = self.opponentMarker
            else:
                marker =self.playerMarker

        try:
            #print('Enter where you would like to place a 0 in the form rownumber,columnnumber: ')
            #instr = input()
            #inList = [int(n) for n in instr.split(',')] 
            coord = (row, col)
            print(coord)
            game_status,board=self.game.move(self.game.turn_monitor,coord)
            print("Legal Move")
            btn = self.master.nametowidget("row{0}_col{1}".format(row, col))
            btn.config(text=marker)
            print(board)
        except Exception as e:
            print("Invalid Move: " + str(e))

        self.CheckGameStatus()


root = Tk()
model = load_model('myModel1.h5')
play = PlayWithGui(root)
play.PlayGame(model)
root.mainloop()
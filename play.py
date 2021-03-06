
from keras.models import load_model
from game.environment import TicTacToeEnvironment
import model.moveSelector as ms

#model = load_model('myModel.h5')

# Play against program
model = load_model('myModel.h5')
print("___________________________________________________________________")
print("Welcome to the Tic Tac Toe Game")
print("You will be playing against the self learned Program")
print("When it is your move, enter the coordinates in the form rownumber,columnnumber")
print(" For example, to place 0 at the top right corner, enter 0,2")
print("___________________________________________________________________")

play_again="Y"
while(play_again=="Y"):
    print("___________________________________________________________________")
    print("Starting a new Game")
    game=TicTacToeEnvironment()
    game.toss()
    print(game.board)
    print(game.turn_monitor," has won the toss")

    while(1):
        if game.game_status()=="In Progress" and game.turn_monitor==0:
            print("Your Turn")
            while(1):
                try:
                    print('Enter where you would like to place a 0 in the form rownumber,columnnumber: ')
                    instr = input()
                    inList = [int(n) for n in instr.split(',')] 
                    coord = tuple(inList)
                    print(coord)
                    game_status,board=game.move(0,coord)
                    print(board)
                    break
                except:
                    print("Invalid Move")
        elif game.game_status()=="In Progress" and game.turn_monitor==1:
            print("Program's turn")
            chosen_move,new_board_state,score=ms.move_selector(model,game.board,game.turn_monitor)
            game_status,board=game.move(game.turn_monitor,chosen_move)
            print(board)
        else:
            break

    if game_status=="Won" and (1-game.turn_monitor)==1: 
        print("Program has won")
    if game_status=="Won" and (1-game.turn_monitor)==0:
        print("You has won")
    if game_status=="Drawn":
        print("Game Drawn")
    print("Would you like to play again?Y/N")
    play_again=input()


game=TicTacToeEnvironment()
game.toss()
print("Player ",game.turn_monitor," has won the toss")
print("Current board state \n",game.board)
legal_moves_dict=legal_moves_generator(game.board,game.turn_monitor)
print("Dictionary of Possible Next Legal Moves:")
pprint.pprint(legal_moves_dict)
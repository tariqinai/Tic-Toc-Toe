# TODO Name if empty going to be Guest
# TODO All variables must be initialize in class
# TODO Loop Up the Multiplayer and Single player Till match Tied or one of the player Wins.
##############
from MultiPlayer import MultiPlayer as mp
from SinglePlayer import SinglePlayer as sp
# Main Body
if __name__ == '__main__':
  while True:
    choice = input("You Wanna play with computer???\n\033[1;34;40m Press y for YES & n for NO && q for QUIT ..... \033[0m")
    masterHistory = []
    ################################
    # Single Player Game
    if choice.lower() =='y':
      print('\033[1;32;40m \t\t##Single Player##\033[0m')
      ticS = SinglePlayer()
      ticS.board()
      historyS = []
      numS = int(input("Enter Your Board Number as mentioned above : "))
    # Multiplayer Game
    elif choice.lower() == 'n':
      print('\033[1;32;40m \t\t##Multi-Player##\033[0m')
      ticM = MultiPlayer()
      ticM.board()
      historyP1 = []
      historyP2 = []
      masterHistory.append(historyP1)
      masterHistory.append(historyP2)
      ###################
      ticM.Input()
      historyP1.append(ticM.num1)
      ticM.boardM( masterHistory)
      ###################
      historyP2.append(ticM.num2)
      ticM.boardM(masterHistory)
      ###################
    # Getting Out of Loop
    elif choice.lower() == 'q':
      break
  print("\033[1;32;40m Thanks For Playing TIC TOC TOE !!! \033[0m ")

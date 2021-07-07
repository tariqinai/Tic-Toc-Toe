# TODO Name if empty going to be Guest
# TODO Loop Up the Multiplayer and Single player Till match Tied or one of the player Wins.
# TODO The rules are going to implement using all() function.
##############
from MultiPlayer import MultiPlayer as mp
from SinglePlayer import SinglePlayer as sp
# Main Body
if __name__ == '__main__':
  while True:
    choice = input("You Wanna play with computer???\n\033[1;34;40m Press y for YES & n for NO && q for QUIT ..... \033[0m")
    ################################
    # Single Player Game
    if choice.lower() =='y':
      print('\033[1;32;40m \t\t##Single Player##\033[0m')
      ticS = sp()
      ticS.board()
      numS = int(input("Enter Your Board Number as mentioned above : "))
    # Multiplayer Game
    elif choice.lower() == 'n':
      print('\033[1;32;40m \t\t##Multi-Player##\033[0m')
      ticM = mp()
      ticM.board()
      ticM.Input()
      ###################
    # Getting Out of Loop
    elif choice.lower() == 'q':
      break
  print("\033[1;32;40m Thanks For Playing TIC TOC TOE !!! \033[0m ")

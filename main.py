# TODO Name if empty going to be Guest
##############
from MultiPlayer import MultiPlayer as mp
from SinglePlayer import SinglePlayer as sp
# Main Body
if __name__ == '__main__':
  while True:
    choice = input("You Wanna play with Computer or Human???\n\033[1;34;40m Press c for Computer & m for MultiPlayer && q for QUIT ..... \033[0m")
    ################################
    # Single Player Game
    if choice.lower() =='c':
      print('\033[1;32;40m \t\t##Single Player##\033[0m')
      ticS = sp()
      ticS.board()
      while True:
        checkS = ticS.Input()
        if checkS == 'b':
          break
    # Multiplayer Game
    elif choice.lower() == 'm':
      print('\033[1;32;40m \t\t##Multi-Player##\033[0m')
      ticM = mp()
      ticM.board()
      while True:
        check = ticM.Input()
        if check == 'b':
          break
      ###################
    # Getting Out of Loop
    elif choice.lower() == 'q':
      break
  print("\033[1;32;40m Thanks For Playing TIC TOC TOE !!! \033[0m ")

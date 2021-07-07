import TicTocToeC as tic

class MultiPlayer(tic):

  def __init__(self):
    super(MultiPlayer, self).__init__()
    self.player2 = input("Player 2 Name : ")
    self.player2Sym = '$'
    self.num2 = 0
    self.historyP2 = 0

  def Input(self):
    self.num1 = int(input(f"{self.player1} Enter Board Number as mentioned above : "))
    self.num2 = int(input(f"{self.player2} Enter Board Number as mentioned above : "))

  def boardM(self, history):
    counter = 0
    for i in range(0,3):
      for j in range(0,3):
        counter += 1
        if counter in history[0] and len(history[0]) != 0 :
          print(self.player1Sym, end='\t')
        elif counter in history[1] and len(history[1]) != 0:
          print(self.player2Sym, end='\t')
        else:
          print('_', end='\t')
      print()

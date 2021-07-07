from TicTocToeC import TicTocToe

class SinglePlayer(TicTocToe):

  def __init__(self):
    super(SinglePlayer, self).__init__()


  def Input(self):
    self.num1 = int(input(f"{self.player1} Enter Board Number as mentioned above : "))
    self.historyP1.append(self.num1)

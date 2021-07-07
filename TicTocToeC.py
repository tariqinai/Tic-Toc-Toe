from abc import abstractmethod as abstract

# Tic Toc Toe
class TicTocToe(object):
  def __init__(self):
    self.player1 = input("Player 1 Name : ")
    self.player1Sym = '#'
    self.num1 = 0
    self.historyP1 = []
    self.masterHistory = []
  @abstract
  def Input(self):
    pass
  def board(self):
    print("The 3-by-3 board is as follows : ")
    n=0
    for i in range(3):
      for j in range(3):
        print(n+1, end='\t')
        n += 1
      print()
    print('Pick A number where you want to Tick.')
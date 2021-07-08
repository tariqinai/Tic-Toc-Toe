from TicTocToeC import TicTocToe

class MultiPlayer(TicTocToe):

  def __init__(self):
    super(MultiPlayer, self).__init__()
    self.player2 = input("Player 2 Name : ")
    if not len(self.player2):
      self.player2 = "Guest2"
    self.player2Sym = '$'
    self.num2 = 0
    self.historyP2 = []
    self.masterHistory.append(self.historyP2)

  def Input(self):
    self.num1 = int(input(f"{self.player1} Enter Board Number as mentioned above : "))
    while self.num1 in self.masterHistory[0] or self.num1 in self.masterHistory[1]:
      self.num1 = int(input(f"{self.player1} Enter a unique Board Number : "))
    self.historyP1.append(self.num1)
    self.boardM(self.masterHistory)
    if len(self.masterHistory[0]) >= 3:
      for i in range(len(self.win)):
        if all(val in self.masterHistory[0] for val in self.win[i]):
          print(f"\033[1;32;40m Congrats {self.player1} you win.\033[0m ")
          return 'b'
        elif len(self.masterHistory[0]) + len(self.masterHistory[1]) == 9:
          print("\033[1;32;40m Game is Drawn.\033[0m ")
          return 'b'

    self.num2 = int(input(f"{self.player2} Enter Board Number as mentioned above : "))
    while self.num2 in self.masterHistory[0] or self.num2 in self.masterHistory[1]:
      self.num2 = int(input(f"{self.player2} Enter a unique Board Number : "))
    self.historyP2.append(self.num2)
    self.boardM(self.masterHistory)
    if len(self.masterHistory[1]) >= 3:
      for i in range(len(self.win)):
        if all(val in self.masterHistory[1] for val in self.win[i]):
          print(f"\033[1;32;40m Congrats {self.player2} you win.\033[0m ")
          return 'b'
        elif len(self.masterHistory[0]) + len(self.masterHistory[1]) == 9:
          print("\033[1;32;40m Game is Drawn.\033[0m ")
          return 'b'

  def boardM(self, history):
    counter = 0
    for i in range(3):
      for j in range(3):
        counter += 1
        if counter in history[0] and len(history[0]) != 0 :
          print(self.player1Sym, end='\t')
        elif counter in history[1] and len(history[1]) != 0:
          print(self.player2Sym, end='\t')
        else:
          print('_', end='\t')
      print()


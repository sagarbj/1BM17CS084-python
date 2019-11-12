def hor():
     print(" --- "*boardsize)
def ver():
     print("|   "*(boardsize+1))
boardsize=int(input("Enter size of a game board ?"))
for i in range(boardsize):
     hor()
     ver()
hor()

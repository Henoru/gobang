from model import *
from board import board
import MCTS
B=board()
print(calc(MCTS.transf(B,(0,0),1)))


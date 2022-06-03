from ML.model import *
from board import board
import ML.MCTS
net=torch.load(".\src\ML\model.pth")
tr=ML.MCTS.MCTS(net,5)
def get_pos(B:board,typ):
  cur=ML.MCTS.node(None,B.acts[-1],1,typ)
  pos=tr.dfsForPlayer(B,cur)
  return pos


    


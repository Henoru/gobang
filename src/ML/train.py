from model import *
from board import board
import MCTS
B=board()
net=CNN()
typ=1
cur=MCTS.node(None,(-1,-1),1,typ)
tr=MCTS.MCTS(net)
#print(calc(B,(0,0),1))
while True:
  ans=tr.dfs(B,cur)
  B.move(ans[0][0],cur.typ)
  if B.is_win(cur.typ) or B.is_full():
    break
  typ=3-typ
  cur=MCTS.node(None,ans[0][0],1,typ)



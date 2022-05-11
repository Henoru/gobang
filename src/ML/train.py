from model import *
from board import board
import MCTS
B=board()
typ=1
cur=MCTS.node(None,(-1,-1),1,typ)
tr=MCTS.MCTS()
while True:
  ans=tr.dfs(B,cur)
  if not B.move(ans[0][0],cur.typ):
    print("haha")
  print(ans[0][0])
  if B.is_win(cur.typ) or B.is_full():
    break
  typ=3-typ
  cur=MCTS.node(None,ans[0][0],1,typ)



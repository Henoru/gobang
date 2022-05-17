from model import *
from board import board
import MCTS
B=board()
net=torch.load("model.pth")
typ=1
cur=MCTS.node(None,(-1,-1),1,typ)
tr=MCTS.MCTS(net)
print(calc(B,(0,0),1,net))
data=[]
while True:
  data.append((B,tr.dfs(B,cur),cur.act,cur.typ))
  if len(cur.chr):
    cur=cur.select()
    B.move(cur.act,cur.fa.typ)
  else:
    train(net,data)
    torch.save(net,"model.pth")
    B=board()
    cur=MCTS.node(None,(-1,-1),1,typ)




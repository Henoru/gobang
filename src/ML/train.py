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
  tr.dfs(B,cur)
  # data.append((B,tr.dfs(B,cur),cur.act,cur.typ))
  test=np.zeros((15,15))
  test[0][0]=1
  data.append((B,test,cur.act,cur.typ))
  if len(cur.chr):
    cur=cur.select()
    B.move(cur.act,cur.fa.typ)
    cur.fa=None
    # sprint(B.bd)
  else:
    train(net,data)
    torch.save(net,"model.pth")
    B=board()
    print(calc(B,(0,0),1,net))
    cur=MCTS.node(None,(-1,-1),1,typ)




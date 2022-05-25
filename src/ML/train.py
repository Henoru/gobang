from model import *
from board import board
import MCTS
B=board()
net=torch.load(".\src\ML\model.pth")
# print(net.state_dict())
typ=1
cur=MCTS.node(None,(-1,-1),1,typ)
tr=MCTS.MCTS(net)
print(calc(B,(0,0),1,net))
data=[]
cnt=0
while True:
  cnt+=1
  data.append((B,tr.dfs(B,cur),cur.act,cur.typ))
  print(cnt,len(data))
  if len(cur.chr):
    cur=cur.select()
    B.move(cur.act,cur.fa.typ)
    cur.fa=None
  else:
    train(net,data)
    data=[]
    # print(net.state_dict())
    torch.save(net,".\src\ML\model.pth")
    B=board()
    print(calc(B,(0,0),1,net))
    cnt=0
    cur=MCTS.node(None,(-1,-1),1,typ)




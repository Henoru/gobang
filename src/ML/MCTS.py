import numpy as np
from board import board
from const import *
from model import calc
#c=5 # UCT搜索策略参数
class node:
  def __init__(self,fa,act,P,typ):
      self.fa=fa  # 结点的父亲
      self.chr=[] # 结点的孩子
      self.W=0    # 子状态总价值
      self.Q=0    # 平均价值 W/N
      self.N=0    # 被访问次数
      self.U=0    # UCT参数
      self.P=P    # 先验概率
      self.act=act # 上一步
      self.typ=typ
  def backup(self,v):
    self.N+=1
    self.W+=v
    self.Q=self.W/self.N
  def select(self):
    index=np.argmax(np.asarray([c.uct() for c in self.chr]))
    return self.chr[index]
  def expand(self,B,net):
      self.chr=[node(self,act,P,3-self.typ) for act,P in calc(B,self.act,self.typ,net)]
  def uct(self):
    return self.Q+CPUCT*self.P*np.sqrt(self.fa.N)/(self.N+1)
def dirichlet_noise(props, eps=DLEPS, alpha=DLALPHA):
  return (1 - eps) * props + eps * np.random.dirichlet(np.full(len(props), alpha))
class MCTS:
  def __init__(self,net,MCTt=MCTSTIMES):
    self.net=net
    self.MCTt=MCTt
  def dfs(self,B_:board,node):
    self.rt=node
    while self.rt.N<self.MCTt:
      # print(self.rt.N)
      cur=self.rt
      B=board(B_)
      win=0
      while True:
        if B.is_win(3-cur.typ):
          win=1
          break
        if len(cur.chr)==0:
          cur.expand(B,self.net)
          if len(cur.chr)==0:
            break
        cur=cur.select()
        #print(cur.act)
        B.move(cur.act,cur.typ)
      while cur:
        cur.backup(win)
        win*=-1
        cur=cur.fa
    ans=np.zeros(15*15)
    for x in self.rt.chr:
      ans[x.act[0]*15+x.act[1]]=x.N/self.rt.N
    # print(ans)
    # dirichlet_noise(ans)
    # print(ans)
    # ans=ans/ans.sum()
    # print(ans)
    return ans
  def dfsForPlayer(self,B_:board,node):
    self.rt=node
    while self.rt.N<self.MCTt:
      cur=self.rt
      B=board(B_)
      win=0
      while True:
        # print("haha")
        if B.is_win(3-cur.typ):
          win=1
          break
        if len(cur.chr)==0:
          cur.expand(B,self.net)
          if len(cur.chr)==0:
            break
        cur=cur.select()
        B.move(cur.act,cur.typ)
      while cur:
        cur.backup(win)
        win*=-1
        cur=cur.fa
    return self.rt.select().act
      

      
    
      

      
    
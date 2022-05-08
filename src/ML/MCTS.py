import numpy as np
from ..board import board
from const import *
c=5 # UCT搜索策略参数
class node:
  def __init__(self,fa,act,P):
      self.fa=fa  # 结点的父亲
      self.chr={} # 结点的孩子
      self.W=0    # 子状态总价值
      self.Q=0    # 平均价值 W/N
      self.N=0    # 被访问次数
      self.U=0    # UCT参数
      self.P=P    # 先验概率
      self.act=act # 上一步
  def backup(self,v):
    self.N+=1
    self.W+=v
    self.Q=self.W/self.N
  def select(self):
    index=np.argmax(np.asarray([c.uct() for c in self.chr]))
    return self.chr[index]
  def expand(self):
    self.chr=[node(self,act,P) for act,P in [(1,2)]]
  def uct(self):
    return self.Q+CPUCT*self.P*np.sqrt(self.fa.N)/(self.N+1)
def dirichlet_noise(props, eps=DLEPS, alpha=DLALPHA):
  return (1 - eps) * props + eps * np.random.dirichlet(np.full(len(props), alpha))
class MCTS:
  def __init__(self,MCTt=MCTSTIMES):
    self.MCTt=MCTt
  def dfs(self,B_:board,node):# 温度 
    self.rt=node
    for _ in range(self.MCTt):
      curnode=self.rt
      B=board(B_)

      while len(curnode.chr):
        curnode=curnode.select()
        B.move(curnode.act)
    
      

      
    
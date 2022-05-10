import numpy as np
class board:
  '棋盘类'
  EMPTY=0
  BLACK=1
  WHITE=2
  def __init__(self,B=0):
    try:
      self.bd=B.bd.copy()
    except:
      self.bd=np.zeros((15,15))
  def __getitem__(self,key):
    return self.bd[key]
  def clear(self):
    '''初始化为空白棋盘'''
    self.bd=np.zeros((15,15))
  def is_win(self,typ)->bool: #tpy玩家是否获得胜利
    '''判断typ类型类是否五子连珠'''
    def win_(line):
      st=0
      for j in range(len(line)):
        if line[j]==typ:
          if j-st>=4:
            return True
        else:
          st=j+1
      return False
    #横连五子
    for i in range(15):
      if win_(self.bd[i,]):
        return True
    #竖连五子
    for i in range(15):
      if win_(self.bd[:,i]):
        return True
    #反对角线方向
    for i in range(15):
      if win_(np.diagonal(self.bd,offset=i)):
        return True
      if i and win_(np.diagonal(self.bd,offset=-i)):
        return True
    #主对角线方向
    temp=np.flip(self.bd,axis=1)
    for i in range(15):
      if win_(np.diagonal(temp,offset=i)):
        return True
      if i and win_(np.diagonal(temp,offset=-i)):
        return True
    return False
  def move(self,pos,typ)->bool: #在pos位置下tpy棋，返回是否成功
    '''落子，在pos位置落typ类型的棋子'''
    x,y=pos[0],pos[1]
    if self[x][y]!=self.EMPTY:
      return False
    self[x][y]=typ
    return True
  def delete(self,pos):
    '''移除pos位置的棋子'''
    x,y=pos[0],pos[1]
    self[x][y]=self.EMPTY
  def is_full(self)->bool:
    '''判断棋盘有无空位置'''
    return np.min(self.bd)!=0
  def is_empty(self):
    '''判断棋盘是否为空棋盘'''
    return np.max(self.bd)==0
class board:
  '棋盘类'
  EMPTY=0
  BLACK=1
  WHITE=2
  def __init__(self):
    self.bd=[[0 for y in range(15)] for x in range(15)]
  def __getitem__(self,key):
    return self.bd[key]
  def write(self): #输出棋盘
    '''在命令行打印棋盘 黑:o 白x'''
    print(" ".join([" "]+[str(x) for x in range(10)]+[chr(ord('A')+x-10) for x in range(10,15)]))
    for i in range(2*15+1):
      if i%2==0:
        print(" ",end="")
      elif i//2 in range(10):
        print(i//2,end="")
      else:
        print(chr(ord('A')+i//2-10),end="")
      for j in range(2*15+1):
        if i%2==0:
          print('-',end="")
        elif j%2==0:
          print('|',end="")
        elif self.bd[i//2][j//2]==self.BLACK:
          print('O',end="")
        elif self.bd[i//2][j//2]==self.WHITE:
          print('X',end="")
        elif self.bd[i//2][j//2]==self.EMPTY:
          print(' ',end="")
      print()
  def clear(self):
    '''初始化为空白棋盘'''
    self.bd=[[0 for y in range(15)] for x in range(15)]
  def is_win(self,typ)->bool: #tpy玩家是否获得胜利
    '''判断typ类型类是否五子连珠'''
    #横连五子
    for i in range(15):
      st=0
      for j in range(15):
        if self[i][j]==typ:
          if j-st>=4:
            return True
        else:
          st=j+1  
    #竖连五子
    for i in range(15):
      st=0
      for j in range(15):
        if self[j][i]==typ:
          if j-st>=4:
            return True
        else:
          st=j+1  
    #斜连五子
    for i in range(15):
      st=0
      for j in range(15-i):
        if self[j][i+j]==typ:
          if j-st>=4:
            return True
        else:
          st=j+1
      st=0
      for j in range(15-i):
        if self[i+j][j]==typ:
          if j-st>=4:
            return True
        else:
          st=j+1
      st=0
      for j in range(i+1):
        if self[j][i-j]==typ:
          if j-st>=4:
            return True
        else:
          st=j+1
      st=0
      for j in range(15-i):
        if self[i+j][14-j]==typ:
          if j-st>=4:
            return True
        else:
          st=j+1
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
    for i in range(15):
      for j in range(15):
        if self[i][j]==self.EMPTY:
          return False
    return True
  def is_empty(self):
    '''判断棋盘是否为空棋盘'''
    for i in range(15):
      for j in range(15):
        if self[i][j]!=self.EMPTY:
          return False
    return True

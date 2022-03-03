class board:
  '棋盘'
  EMPTY=0
  BLACK=1
  WHITE=2
  def __init__(self):
    self.bd=[[0 for y in range(15)] for x in range(15)]
    self.pos_left=15*15
  def write(self): #输出棋盘
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
    self.bd=[[0 for y in range(15)] for x in range(15)]
  def is_win(self,typ)->bool: #tpy玩家是否获得胜利
    #横连五子
    for i in range(15):
      st=0
      for j in range(15):
        if self.bd[i][j]==typ:
          if j-st>=4:
            return True
        else:
          st=j+1  
    #竖连五子
    for i in range(15):
      st=0
      for j in range(15):
        if self.bd[j][i]==typ:
          if j-st>=4:
            return True
        else:
          st=j+1  
    #斜连五子
    for i in range(15):
      st=0
      for j in range(15-i):
        if self.bd[j][i+j]==typ:
          if j-st>=4:
            return True
        else:
          st=j+1
      st=0
      for j in range(15-i):
        if self.bd[i+j][j]==typ:
          if j-st>=4:
            return True
        else:
          st=j+1
      st=0
      for j in range(i+1):
        if self.bd[j][i-j]==typ:
          if j-st>=4:
            return True
        else:
          st=j+1
      st=0
      for j in range(15-i):
        if self.bd[i+j][14-j]==typ:
          if j-st>=4:
            return True
        else:
          st=j+1
    return False
  def move(self,pos,tpy)->bool: #在pos位置下tpy棋，返回是否成功
    x,y=pos[0],pos[1]
    if self.bd[x][y]!=self.EMPTY:
      return False
    self.bd[x][y]=tpy
    self.pos_left=self.pos_left-1
    return True

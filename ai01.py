from board import board

#搜索版AI
depth=4 #最大搜索深度
cnt=0
INF=1000000000 #最大值
def calc(typ,lst):
  #连五 10000000
  #活：(4,10000) (3,1000) (2,100) (1,10)
  scr=(1,10,100,1000,10000,10000000)
  #死：(4,1000) (3,100) (2,10) (1,1)
  EMPTY=0
  t=3-typ
  num=0
  ans=0
  for x in lst:
    if x!=typ:
      if num>=5:
        ans=ans+scr[5]
      elif num==0:
        None
      elif t==EMPTY and x==EMPTY: #活分
        ans=ans+scr[num]
      elif t==EMPTY or x==EMPTY: #死分
        ans=ans+scr[num-1]
      t=x
      num=0
    else:
      num=num+1
  if num>=5:
    ans=ans+scr[5]
  elif num!=0 and t==EMPTY:
    ans=ans+scr[num-1]
  return ans
def evaluate(B:board,typ)->int:
  ans=0
  for i in range(15):
    #横向搜索
    ans=ans+calc(typ,[B.bd[i][j] for j in range(15)])
    #纵向搜索
    ans=ans+calc(typ,[B.bd[j][i] for j in range(15)])
    #右斜方向搜索
    ans=ans+calc(typ,[B.bd[j][i+j] for j in range(15-i)])
    if i!=14:
      ans=ans+calc(typ,[B.bd[14-j][i-j] for j in range(i+1)])
    #左斜方向搜搜
    ans=ans+calc(typ,[B.bd[j][i-j] for j in range(i+1)])
    if i!=0:
      ans=ans+calc(typ,[B.bd[14-j][i+j] for j in range(15-i)])
  return ans
def min_max_dfs(B:board,typ,d,alpha=-INF,beta=-INF): #棋盘 当前执方 当前深度
  global cnt
  cnt=cnt+1
  if cnt%1000==0:
    print(cnt)
  if d==depth:
    return (evaluate(B,typ)-evaluate(B,3-typ),(-1-1))
  search_list=[]
  dx=[-1,-1,-1, 0, 0, 1, 1, 1]
  dy=[-1, 0, 1,-1, 1,-1, 0, 1]
  for i in range(15):
    for j in range(15):
      found=False
      for k in range(8):
        if i+dx[k] in range(15) and j+dy[k] in range(15) and B.bd[i+dx[k]][j+dy[k]]!=B.EMPTY:
          found=True
          break
      if found and B.move((i,j),typ):
        search_list.append((evaluate(B,typ)-evaluate(B,3-typ),(i,j)))
        B.delete((i,j))
  search_list.sort(reverse=True)
  width=10
  anspos=(-1,-1)
  ans=-INF
  for i in range(min(len(search_list),width)):
    pos=search_list[i][1]
    if B.move(pos,typ):
      if B.is_win(typ):
        B.delete(pos)
        return (INF//2,pos)
      get=-min_max_dfs(B,3-typ,d+1,alpha,beta)[0]
      B.delete(pos)
      #print(d,pos,get)
      if d%2==0:
        alpha=max(alpha,get)
      else:
        beta=max(beta,get)
      if -beta<=alpha:
        return (get,pos)
      if get>ans:
        ans=get
        anspos=pos
  return (ans,anspos)
def get_pos(B:board,typ):
  if B.is_empty():
    return (7,7)
  return min_max_dfs(B,typ,0)[1]

import os
from board import board
import pygame


# 命令行版本
def clear():
  os.system('cls')
def get_pos_from_terminals(pos):
  x,y=-1,-1
  if len(pos)!=2:
    return (x,y)
  if pos[0] in [str(x) for x in range(10)]:
    x=int(pos[0])
  if pos[1] in [str(x) for x in range(10)]:
    y=int(pos[1])
  if ord(pos[0])-ord('A') in range(5):
    x=ord(pos[0])-ord('A')+10
  if ord(pos[1])-ord('A') in range(5):
    y=ord(pos[1])-ord('A')+10
  return x,y
def new_game_at_terminals()->bool:
  B=board()
  cnt=1
  while True:
    B.write()
    print("Player{}:".format(cnt))
    pos=get_pos_from_terminals(input())
    clear()
    if pos[0]==-1 or pos[1]==-1:
      continue
    if not B.move(pos,cnt):
      continue
    if B.is_win(cnt):
      print("Player{} win!!!".format(cnt))
      return True
    cnt=3-cnt
def play_at_terminals():
  while new_game_at_terminals():
    print("按下回车继续游戏;输入q退出游戏")
    if input()[0]=='q':
      break


# 图形界面版本 可以直接改(应该)
padding_top=50    #棋盘上边距
padding_left=50   #棋盘左边距
line_gap=30       #棋盘线距离
chess_size=5      #棋子大小
chess_colors=[(0,0,0),(255,255,255)] #棋子颜色
#点的坐标
rows=[padding_top+i*line_gap for i in range(15)]
cols=[padding_left+j*line_gap for j in range(15)]
points=[[(cols[j],rows[i]) for j in range(15)] for i in range(15)]

def draw_a_line(screen,points):
  pygame.draw.lines(screen, (0,0,0), False,points,1)
def draw_lines(screen,points):
  for point in points:
    draw_a_line(screen,point)
def draw_chess(screen,point,typ):
  pygame.draw.circle(screen,chess_colors[typ-1],point,2*chess_size,0) 
def get_pos_from_mouse(pos):
  x,y=-1,-1
  for i in range(15):
    if abs(rows[i]-pos[1])<=chess_size:
      x=i
    if abs(cols[i]-pos[0])<=chess_size:
      y=i
  return x,y
Mod=0 #模式选择 [PVP PVC CVP CVC] 默认为PVP
# 画菜单栏
def draw_menu(screen):
  screen.fill((229,182,112))
  w=cols[14]+padding_left
  h=rows[14]+padding_top
  fontTitle=pygame.font.Font(r'Font\Bustracks-FREE-3.ttf',150)
  fontMod=pygame.font.Font(r'Font\Bustracks-FREE-3.ttf',40)
  titleFont=fontTitle.render("Gobang",True,(255,0,0))
  tw,th=titleFont.get_size() #标题大小
  screen.blit(titleFont,(w/2-tw/2,h/4-th/2))
  Modchoice=["Player Vs Player","Player Vs Computer","Computer Vs Player","Computer Vs Computer"]
  Modchoice[Mod]=Modchoice[Mod]
  Modchoicefont=[fontMod.render(Modchoice[i],True,(0,0,0) if Mod==i else (127,127,127)) for i in range(4)]
  sumhh=0
  for i in range(4):
    ww,hh=Modchoicefont[i].get_size()
    screen.blit(Modchoicefont[i],(w/2-ww/2,h/2+sumhh))
    sumhh=sumhh+hh+5
  pygame.display.flip()
def draw_win_title(screen,win):
  w=cols[14]+padding_left
  h=rows[14]+padding_top
  winner=[("Black","White","Nobody")]
  background_color=[(255,255,255),(0,0,0),(100,100,100)]
  font_color=[(0,0,0),(255,255,255),(255,0,0)]
  fontTitle=pygame.font.Font(r'Font\Bustracks-FREE-3.ttf',80)
  titleFont=fontTitle.render(winner[Mod][win-1]+" win",True,font_color[win-1])
  tw,th=titleFont.get_size() #标题大小
  pygame.draw.rect(screen,background_color[win-1],(0,h/2-th/2-10,w,th+20))
  screen.blit(titleFont,(w/2-tw/2,h/2-th/2))
  pygame.display.flip()
def new_game_at_gui(screen):
  B=board()
  global Mod
  draw_menu(screen)
  get_Enter=False
  while not get_Enter:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
      elif event.type==pygame.KEYDOWN:
        if event.key==13:
          get_Enter=True
        elif event.key==119:
          Mod=(Mod+3)%4
          draw_menu(screen)
        elif event.key==115:
          Mod=(Mod+1)%4
          draw_menu(screen)
  screen.fill((229,182,112))
  draw_lines(screen,points)
  draw_lines(screen,[[points[i][j] for i in range(15)] for j in range(15)])
  pygame.display.flip()
  cnt=1
  win=0
  while not win:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
      elif event.type==pygame.MOUSEBUTTONDOWN:
        pos=get_pos_from_mouse(event.pos)
        if pos[0]==-1 or pos[1]==-1:
          continue
        if B.move(pos,cnt):
          draw_chess(screen,points[pos[0]][pos[1]],cnt)
          pygame.display.flip()
          if B.is_win(cnt):
            win=cnt
            break
          if B.pos_left==0:
            win=3
            break
          cnt=3-cnt
  draw_win_title(screen,win)
  #按任意键开始新游戏 懒得新建一个变量
  get_Enter=False
  while not get_Enter:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
      elif event.type==pygame.KEYDOWN:
        get_Enter=True
  return True
#图形界面初始化和游戏循环过程
def play_with_gui():
  pygame.init()
  screen=pygame.display.set_mode((cols[14]+padding_left,rows[14]+padding_top))
  while new_game_at_gui(screen):
    None
play_with_gui()

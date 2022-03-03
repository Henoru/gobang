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


# 图形界面版本
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
def new_game_at_gui(screen):
  B=board()
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
          cnt=3-cnt
  return True
def play_with_gui():
  pygame.init()
  screen=pygame.display.set_mode((600,600))
  fontMod=pygame.font.Font(r'Font\思源宋体.otf',100)
  fontInfo=pygame.font.Font(r'Font\思源宋体.otf',100)
  Mod=0
  while True:
    None
play_with_gui()

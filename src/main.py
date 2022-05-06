import os
from board import board
import pygame
#import ai01
import ai02 as ai           # AI模块
from graphics import *      # 图形化模块
# 命令行版本(已废用)
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

Mod=0 #模式选择 [PVP PVC CVP CVC] 默认为PVP
# 画菜单栏
def get_pos(B:board,typ,player_typ):
  pos=(-1,-1)
  if player_typ==0:
    while pos[0]==-1 or pos[1]==-1:
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          pygame.quit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
          pos=get_pos_from_mouse(event.pos)
  else:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
    pos=ai.get_pos(B,typ)
  return pos
def choose_Mod(screen):
  global Mod
  draw_menu(screen,Mod)
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
          draw_menu(screen,Mod)
        elif event.key==115:
          Mod=(Mod+1)%4
          draw_menu(screen,Mod)
def new_game_at_gui(screen):
  switch_chess_typ=lambda typ:3-typ
  B=board() # 初始化棋盘
  # 模式选择
  global Mod
  choose_Mod(screen)
  draw_borad(screen)
  cnt=board.BLACK #黑棋先手
  win=0
  player=[0,(Mod//2)%2,Mod%2] #Mod[0,3] 两位二进制位表示黑棋和白棋的棋手是玩家还是人机
  pygame.display.flip()
  while not win:
    #B.write()
    pos=get_pos(B,cnt,player[cnt])
    if B.move(pos,cnt):
      draw_chess(screen,pos,cnt)
      pygame.display.flip()
      if B.is_win(cnt):
        win=cnt
        break
      if B.is_full():
        win=3 #平局
        break
      cnt=switch_chess_typ(cnt)
  draw_win_title(screen,win)
  #按任意键开始新游戏 懒得新建一个变量
  get_Enter=False
  while not get_Enter:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
      elif event.type==pygame.KEYDOWN:
        get_Enter=True
      elif event.type==pygame.MOUSEBUTTONDOWN:
        get_Enter=True
  return True
#图形界面初始化和游戏循环过程
def play_with_gui():
  screen=graphics_init()
  while new_game_at_gui(screen):
    None
play_with_gui()

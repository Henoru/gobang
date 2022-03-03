import os
from board import board
import pygame
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
def new_game_at_gui():
  return True
def play_with_gui():
  pygame.init()
  screen=pygame.display.set_mode((1000,1000))
  pygame.display.flip()
  while new_game_at_gui():

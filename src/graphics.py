import pygame
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
def draw_chess(screen,pos,typ):
  point=points[pos[0]][pos[1]]
  pygame.draw.circle(screen,chess_colors[typ-1],point,2*chess_size,0) 
def get_pos_from_mouse(event_pos):
  x,y=-1,-1
  for i in range(15):
    if abs(rows[i]-event_pos[1])<=chess_size:
      x=i
    if abs(cols[i]-event_pos[0])<=chess_size:
      y=i
  return x,y
def draw_menu(screen,Mod):
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
  winner=("Black","White","Nobody")
  background_color=((255,255,255),(0,0,0),(100,100,100))
  font_color=((0,0,0),(255,255,255),(255,0,0))
  fontTitle=pygame.font.Font(r'Font\Bustracks-FREE-3.ttf',80)
  titleFont=fontTitle.render(winner[win-1]+" win",True,font_color[win-1])
  tw,th=titleFont.get_size() #标题大小
  pygame.draw.rect(screen,background_color[win-1],(0,h/2-th/2-10,w,th+20))
  screen.blit(titleFont,(w/2-tw/2,h/2-th/2))
  pygame.display.update()
def draw_borad(screen):
  screen.fill((229,182,112))
  draw_lines(screen,points)
  draw_lines(screen,[[points[i][j] for i in range(15)] for j in range(15)])
  pygame.display.flip()
def graphics_init():
  pygame.init()
  screen=pygame.display.set_mode((cols[14]+padding_left,rows[14]+padding_top))
  icon=pygame.image.load("img/04.png")
  pygame.display.set_icon(icon)
  pygame.display.set_caption("Gobang","dudulu")
  return screen
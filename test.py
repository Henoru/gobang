import imp
from sympy import evaluate
from board import board
import ai01
import ai02

typ=1
B=board()
while True:
  print(ai01.get_pos(B,typ))
  pos=ai02.get_pos(B,typ)
  B.move(pos,typ)
  print(pos)
  typ=3-typ

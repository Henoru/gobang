from sympy import tensor
from board import board
import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F

size=15
num_class=size*size
num_epochs=3
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class ResidualBlock(torch.nn.Module):
    def __init__(self,in_channels,out_channels):
        super(ResidualBlock,self).__init__()
        self.conv1 = torch.nn.Conv2d(in_channels,out_channels,kernel_size=5,padding=2)
        self.conv2 = torch.nn.Conv2d(in_channels,out_channels,kernel_size=5,padding=2)
    
    def forward(self, x):
        y = F.relu(self.conv1(x))
        y = self.conv2(y)
        return F.relu(x+y)

class CNN(nn.Module):
  def __init__(self):
    super(CNN,self).__init__()
    self.conv1=nn.Sequential(
      nn.Conv2d(4,16,5,1,2),
      nn.ReLU(),
    )
    self.cconv2=nn.Sequential(
      nn.Conv2d(16,32,5,1,2),
      nn.ReLU(),
      nn.MaxPool2d(kernel_size=2),
    )
    self.conv3=nn.Sequential(
      ResidualBlock(32,32),
      nn.MaxPool2d(kernel_size=2),
    )
    # self.conv4=ResidualBlock(32,32)
    # self.conv5=ResidualBlock(32,32)
    # self.conv6=ResidualBlock(32,32)
    self.conv7=ResidualBlock(32,32)
    self.conv8=self.conv2=nn.Sequential(
      nn.Conv2d(32,16,5,1,2),
      nn.ReLU(),
    )
    self.out=nn.Linear(144,15*15)
  def forward(self,x):
    x=x.to(torch.float32)
    x=self.conv1(x)
    x=self.cconv2(x)
    x=self.conv3(x)
    # x=self.conv4(x)
    # x=self.conv5(x)
    # x=self.conv6(x)
    x=self.conv7(x)
    x=self.conv8(x)
    x=x.reshape(-1)
    output=self.out(x)
    return output
def transf(B,pos,typ):
  blk=np.where(B.bd==board.BLACK,1,0)
  wht=np.where(B.bd==board.WHITE,1,0)
  epy=np.zeros((15,15))
  if pos[0]!=-1: 
    epy[pos[0]][pos[1]]=1
  if typ==1:
    T=np.zeros((15,15))
  else:
    T=np.ones((15,15))
  ans=np.concatenate([blk,wht,epy,T]).reshape((4,15,15))
  return torch.from_numpy(ans)
def train(net,data):
  def update(input,P):
    input=torch.from_numpy(input)
    p=P.copy()
    p=torch.from_numpy(np.reshape(p,(15*15)))   
    output=net(input)
    loss=nn.CrossEntropyLoss(output,p)
    loss.backward()
    opt.step()
    opt.zero_grad()
  lr_rate=0.02
  opt=torch.optim.SGD(net.parameters(),lr=lr_rate,weight_decay=2)
  for B,P,pos,typ in data:
    P=np.reshape(P,(15,15))
    blk=np.where(B.bd==board.BLACK,1,0)
    wht=np.where(B.bd==board.WHITE,1,0)
    epy=np.zeros((15,15))
    if pos[0]!=-1: 
      epy[pos[0]][pos[1]]=1
    if typ==1:
      T=np.zeros((15,15))
    else:
      T=np.ones((15,15))
    # identity
    input=np.concatenate([blk,wht,epy,T]).reshape((4,15,15))
    update(input,P)
    # rot90
    input=np.concatenate([np.rot90(blk,1),np.rot90(wht,1),np.rot90(epy,1),T]).reshape((4,15,15))
    update(input,np.rot90(P,1))
    # rot180
    input=np.concatenate([np.rot90(blk,2),np.rot90(wht,2),np.rot90(epy,2),T]).reshape((4,15,15))
    update(input,np.rot90(P,2))
    # rot270
    input=np.concatenate([np.rot90(blk,3),np.rot90(wht,3),np.rot90(epy,3),T]).reshape((4,15,15))
    update(input,np.rot90(P,3))
    # flip
    blk,wht,epy,P=np.flip(blk),np.flip(wht),np.flip(epy),np.flip(P)
    # identity flip
    input=np.concatenate([blk,wht,epy,T]).reshape((4,15,15))
    update(input,P)
    # rot90 flip
    input=np.concatenate([np.rot90(blk,1),np.rot90(wht,1),np.rot90(epy,1),T]).reshape((4,15,15))
    update(input,np.rot90(P,1))
    # rot180 flip
    input=np.concatenate([np.rot90(blk,2),np.rot90(wht,2),np.rot90(epy,2),T]).reshape((4,15,15))
    update(input,np.rot90(P,2))
    # rot270 flip
    input=np.concatenate([np.rot90(blk,3),np.rot90(wht,3),np.rot90(epy,3),T]).reshape((4,15,15))
    update(input,np.rot90(P,3))
  data=[]
def calc(B:board,pos,typ,net):
  B_=board(B)
  _=transf(B,pos,typ)
  ans=net(_).detach().numpy()
  return [((i,j),ans[i*15+j]) for i in range(15) for j in range(15) if B_.move((i,j),1)]
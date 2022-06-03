from board import board
import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F
from torch.utils.data import Dataset
from torch.utils.data import _utils

size=15
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
class CNN(nn.Module):
  def __init__(self):
    super(CNN,self).__init__()
    self.conv_1=nn.Sequential(
      nn.Conv2d(in_channels=4, out_channels=8, kernel_size=3, padding=0),
      nn.ReLU(),
    )
    self.conv_2=nn.Sequential(
      nn.Conv2d(in_channels=8, out_channels=64, kernel_size=3, padding=0),
      nn.ReLU(),
      nn.MaxPool2d(kernel_size=2),
    )
    self.conv_3=nn.Sequential(
      nn.Conv2d(64,256, 3, 1, 0),
      nn.ReLU(),
    )
    self.conv_4=nn.Sequential(
      nn.Conv2d(256,512, 3, 1, 0),
      nn.ReLU(),
    )
    self.out=nn.Sequential(
      nn.Linear(512,225),
      nn.Softmax(dim=1),
    )
  def forward(self,x):
    x=x.to(torch.float32)
    x=self.conv_1(x)
    x=self.conv_2(x)
    x=self.conv_3(x)
    x=self.conv_4(x)
    x = x.view(x.size(0), -1)
    x=self.out(x)
    return x
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
  ans=np.concatenate([blk,wht,epy,T]).reshape((1,4,15,15))
  return torch.from_numpy(ans)
class Mydata(Dataset):
  def __init__(self,data):
    self.data=data
  def __len__(self):
    return len(self.data)*8
  def __getitem__(self,index):
    n,m=index//8,index%8
    B,P,pos,typ=self.data[n]
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
    # flip
    if m%2:
      blk,wht,epy,P=np.flip(blk),np.flip(wht),np.flip(epy),np.flip(P)
    m/=2
    # identity
    input=np.concatenate([np.rot90(blk,m),np.rot90(wht,m),np.rot90(epy,m),T]).reshape((4,15,15))
    P=np.rot90(P,m)
    P=np.reshape(P,-1)
    return torch.from_numpy(input.copy()),torch.from_numpy(P.copy())
def train(net,data):
  torch.set_grad_enabled(True)
  Data=Mydata(data)
  Datas=torch.utils.data.DataLoader(Data,batch_size=10,shuffle=True,drop_last=False)
  lr_rate,epochs=0.01,200
  opt=torch.optim.SGD(net.parameters(),lr=lr_rate,weight_decay=1)
  # criteria=nn.CrossEntropyLoss()
  loss_func=nn.LogSoftmax(dim=1)
  for epoch in range(epochs):
    for i,data_ in enumerate(Datas):
      opt.zero_grad()
      I,O=data_
      output=net(I)
      Loss=(-output*loss_func(O)).sum()
      Loss.backward()
      opt.step()
    if epoch%10==0:
      print("Epoch {}:{}".format(epoch,Loss))
def calc(B:board,pos,typ,net):
  B_=board(B)
  _=transf(B,pos,typ)
  ans=net(_).detach().numpy().reshape(-1)
  return [((i,j),ans[i*15+j]) for i in range(15) for j in range(15) if B_.move((i,j),1)]
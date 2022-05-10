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
    self.conv4=ResidualBlock(32,32)
    self.conv5=ResidualBlock(32,32)
    self.conv6=ResidualBlock(32,32)
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
    x=self.conv4(x)
    x=self.conv5(x)
    x=self.conv6(x)
    x=self.conv7(x)
    x=self.conv8(x)
    x=x.reshape(-1)
    output=self.out(x)
    return output
net=CNN()
def calc(B:board,net=net):
  ans=net.forward(B).detach().numpy()
  B_=board(B)
  return [((i,j),ans[i*15+j]) for i in range(15) for j in range(15) if B_.move((i,j),1)]
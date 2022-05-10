import torch
import torch.nn as nn
import numpy as np

size=15
num_class=size*size
num_epochs=3
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
class CNN(nn.Module):
  def __init__(self):
    super(CNN,self).__init__()
    self.conv1=nn.Sequential(
      nn.Conv2d(4,16,5,1,2),
      nn.ReLU(),
      nn.MaxPool2d(kernel_size=2),
    )
    self.conv2=nn.Sequential(
      nn.Conv2d(16,32,3,1,1 n )
      nn.ReLU(),
      nn.MaxPool2d(kernel_size=2),
    )
    self.out()
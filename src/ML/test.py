import torch.nn as nn
import torch
import model
import numpy as np
def weight_init(m):
  if isinstance(m,nn.Linear):
    nn.init.xavier_normal_(m.weight)
    nn.init.constant_(m.bias,0)
  elif isinstance(m,nn.Conv2d):
    nn.init.kaiming_normal_(m.weight,mode='fan_out',nonlinearity='relu')
C=model.CNN()
# print(C.parameters())
torch.save(C,".\src\ML\model.pth")
# a=torch.tensor([0.,0.,1.],dtype=torch.float32)
# print(nn.LogSoftmax(dim=-1)(a))

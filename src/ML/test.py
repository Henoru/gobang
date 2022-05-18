import torch.nn as nn
import torch
import model
import numpy as np
# C=model.CNN()
# print(C.parameters())
# torch.save(C,"model.pth")
a=torch.tensor([0.,0.,1.],dtype=torch.float32)
print(nn.LogSoftmax(dim=-1)(a))

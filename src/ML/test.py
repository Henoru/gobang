import torch
import model
import numpy as np
C=model.CNN()
torch.save(C,"model.pth")
